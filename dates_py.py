#time is linear
# datetime also check validity of date to exist
# https://docs.python.org/2/library/datetime.html

import datetime as dt

x=dt.datetime.now()
print x
print x.year
print x.strftime("%A")

y=dt.datetime.today()
print y

#creating gnew date object
x= dt.datetime(2018, 6, 1)
print x.strftime("%B")



d1="10/12/2017"
d2="9/11/2018"
print max(d1,d2)

# print d2 - d1 -- doesnt work cause both are string
dd=dt.datetime("10/12/2017")
ddd=dt.datetime("9/11/2018")

print ddd - dd




#.total_seconds()
#.days()
#.time() to extracts time from a date
#.timedelta() used ot calculate new data and time from a given date, cant use timedelta on time object as we may not know if days have passed







# Directive	Description	Example	
# %a	Weekday, short version	Wed	
# %A	Weekday, full version	Wednesday	
# %w	Weekday as a number 0-6, 0 is Sunday	3	
# %d	Day of month 01-31	31	
# %b	Month name, short version	Dec	
# %B	Month name, full version	December	
# %m	Month as a number 01-12	12	
# %y	Year, short version, without century	18	
# %Y	Year, full version	2018	
# %H	Hour 00-23	17	
# %I	Hour 00-12	05	
# %p	AM/PM	PM	
# %M	Minute 00-59	41	
# %S	Second 00-59	08	
# %f	Microsecond 000000-999999	548513	
# %z	UTC offset	+0100	
# %Z	Timezone	CST	
# %j	Day number of year 001-366	365	
# %U	Week number of year, Sunday as the first day of week, 00-53	52	
# %W	Week number of year, Monday as the first day of week, 00-53	52	
# %c	Local version of date and time	Mon Dec 31 17:41:00 2018	
# %x	Local version of date	12/31/18	
# %X	Local version of time	17:41:00	
# %%	A % character



#bucketing time
#-------------------

