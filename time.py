import datetime
import pytz
#datetime.date() , year month and date
d=datetime.date(2020,1,9)#cannot use 01 and 09 leading zeros in decimal integer literals are not permitted;dont give file name as module name

print(d)
tday = datetime.date.today() #printtodaydate
print(tday)
print(tday.year)
print(tday.day)
print(tday.month) #printing month

print(tday.weekday())#0 for monday
print(tday.isoweekday())#1 for monday

time_delta=datetime.timedelta(days=7)
print(tday + time_delta)#2020-01-16 , 7 days ahead
print (tday - time_delta) #, 7 days before

bday=datetime.date(2020 , 7 ,9)
days_left=bday - tday
print (days_left.days)

#datetime.time() hours, minute , seconds , microseconds
t=datetime.time(11, 40, 40, 10)
print(t)#naive

#datetime.datetime gives year months date hour minute seconds microseconds
dt=datetime.datetime(2019, 1, 9, 11, 43, 12, 10)
print(dt)
print(dt.date().year)
print(dt.time().minute)#better to use datetime
print(dt.year)
print(dt.hour)#better use directly

time_delta2=datetime.timedelta(days=10)
print(time_delta2 + dt)

time_delta3=datetime.timedelta(hours=10)
print(time_delta3 + dt)

dt_today=datetime.datetime.today()
dt_now=datetime.datetime.now()
dt_utcnow=datetime.datetime.utcnow()
print(dt_today)
print(dt_now)
print(dt_utcnow)#all are same as of now , we will use pytz for efficience
#use utc recommended
#dt=datetime.datetime(2020,1,9,12,11,45,tzinfo=pytz.UTC)
#print(dt)
dt_utcnow=datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow)##most preferred way , we should use this
#dt_utcnow=datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
#print(dt_utcnow)

dt_mtn=dt_utcnow.astimezone(pytz.timezone('Asia/Kolkata'))#converting from local to others
print(dt_mtn.isoformat())##international standars
#use format codes from doc
print(dt_mtn.strftime('%B %d, %Y'))
dt_str= 'January 10, 2020'
dt =datetime.datetime.strptime(dt_str,'%B %d, %Y')
print (dt)

#strftime -Datetime to string
#strptime - string to Datetime
#arrow popular python package 


####naive to local is pending ...




#for tz in pytz.all_timezones:
 #   print(tz) #all time zones














