# anaysis chrome history

## location of chrome history
/home/jhy/.config/google-chrome/Default

## covert timestamp
last_visit_time: unit us, start time:1601.01.01 00:00:00

last_vist_time/10**6 - 11644473600

gmtime() -- convert seconds since Epoch to UTC tuple

ctime() -- convert time in seconds to string

```python
>>> time.gmtime(0)
time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)
>>> 
>>> time.gmtime(-11644473600)
time.struct_time(tm_year=1601, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=0, tm_yday=1, tm_isdst=0)
>>>
>>> time.ctime(0)
'Thu Jan  1 08:00:00 1970'
>>> time.ctime(-11644473600)
'Mon Jan  1 08:05:43 1601'
>>>
```

## flask bootstrap table
[flask-bootstrap-table](https://github.com/bambooom/flask-bootstrap-table)

## flask-sqlalchemy
[flask-sqlalchemy](http://www.pythondoc.com/flask-sqlalchemy/quickstart.html)

