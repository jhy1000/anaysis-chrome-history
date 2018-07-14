# coding:utf-8

from flask import Flask, jsonify, request
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
import time


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////root/anaysis-chrome-history/History"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

columns = [
        {
            "field":"id",
            "title":"id",
            "sortable":True,
            "width":"5%",
        },
        {
            "field":"url",
            "title":"url",
            "sortable":True,
            "width":"35%",
        },
        {
            "field":"title",
            "title":"title",
            "sortable":True,
            "width":"30%",
        },
        {
            "field":"visit_count",
            "title":"visit_count",
            "sortable":True,
            "width":"5%",
            "visible":False,
        },
        {
            "field":"typed_count",
            "title":"typed_count",
            "sortable":True,
            "width":"5%",
            "visible":False,
        },
        {
            "field":"last_visit_time",
            "title":"last_visit_time",
            "sortable":True,
            "width":"10%",
        },
        {
            "field":"hidden",
            "title":"hidden",
            "sortable":True,
            "width":"5%",
            "visible":False,
        },
        {
            "field":"favicon_id",
            "title":"favicon_id",
            "sortable":True,
            "width":"5%",
            "visible":False,
        }]


class Urls(db.Model):

    __tablename__ = "urls"
    id = db.Column(db.Integer,primary_key=True)
    url = db.Column(db.String(1000))
    title = db.Column(db.String(1000))
    visit_count = db.Column(db.Integer)
    typed_count = db.Column(db.Integer)
    last_visit_time = db.Column(db.Integer)
    hidden = db.Column(db.Integer)
    favicon_id = db.Column(db.Integer)

    @property
    def serialize(self):
        return {
                "id" : self.id,
                "url" : "<div style=\"width:300px;overflow:hidden;text-overflow: ellipsis;white-space:nowrap;\"><a href=\"" + self.url + "\">" + self.url + "</a></div>",
                "title" : "<div style=\"width:300px;overflow:hidden;text-overflow: ellipsis;white-space:nowrap;\">"+self.title+"</div>",
                "visit_count" : self.visit_count,
                "typed_count" : self.typed_count,
                "last_visit_time" : time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime(self.last_visit_time/10**6-11644473600)),
                "hidden" : self.hidden,
                "favicon_id" : self.favicon_id
        }


@app.route('/')
def index():
    urls = [i.serialize for i in Urls.query.all()]
    return render_template("index.html",data=urls,columns=columns,title="Anaysis Chrome History")

if __name__ == '__main__':
    app.run(debug=True)

