import datetime as dt
import time
# time is linear
# https://docs.python.org/2/library/datetime.html

#there are two kinds of date and time naive and aware
# An aware object has sufficient knowledge of applicable algorithmic and political time adjustments, 
# such as time zone and daylight saving time information, to locate itself relative to other aware objects. 
# An aware object is used to represent a specific moment in time that is not open to interpretation
# A naive object does not contain enough information to unambiguously locate itself relative to other date/time objects. 
# Whether a naive object represents Coordinated Universal Time (UTC), local time, or time in some other timezone is purely 
# up tot the program, just like its up to the program whether a particular mumber represent meters, miles or mass
# Naive objects are easy to understand and to work with, at the cost of ignoring some aspects of reality.

# datetime also check validity of date to exist

#datetime module has followig constants
print '--------------- Current date -------------------'
print 'Now : ' + str(dt.datetime.now())
print 'Now from time : ' + str(dt.date.fromtimestamp(time.time()))
print 'current day : ' + str(dt.datetime.now().day)
print 'current month : ' + str(dt.datetime.now().month)
print 'current year : ' + str(dt.datetime.now().year)
print 'current local date : ' + str(dt.date.today())


#print dt.fromtimestamp(dt.time.time())
print '-------------- Date time constant --------------------'

print 'Date time object constants'
print 'Max year : ' + str(dt.MAXYEAR)
print 'Min year : ' + str(dt.MINYEAR)

print '--------------- constructing date from value -------------------'
print dt.datetime(2020, 5, 17)

print '--------------extracting/formatting values from date--------------------'
dd=dt.datetime(2020, 11, 17, 11, 53)
print 'date : ' + str(dd)
print  'day : ' + str(dd.day)
print 'month : ' + str(dd.month)
print 'year : ' + str(dd.year)

print 'weekday : '+ str(dd.strftime("%A"))
print 'weekday : '+ str(dd.strftime("%a"))
print 'weekday : ' + str(dd.strftime("%w"))
print 'Day of month : ' + str(dd.strftime("%d"))
print 'Month : ' + str(dd.strftime("%B"))
print 'Month : ' + str(dd.strftime("%b"))
print 'Month : ' + str(dd.strftime("%m"))
print 'Year : ' + str(dd.strftime("%y"))
print 'Year : ' + str(dd.strftime("%Y"))
print 'Hour : ' + str(dd.strftime("%H"))
print 'Hour : ' + str(dd.strftime("%I"))
print 'AM/PM : ' + str(dd.strftime("%p"))

print 'Minute : ' + str(dd.strftime("%M"))
print 'Second : ' + str(dd.strftime("%S"))
print 'Microsecond : ' + str(dd.strftime("%f"))
print 'UTC offset : ' + str(dd.strftime("%z"))
print 'Timezone : ' + str(dd.strftime("%Z"))
print 'Day number of year 001-366 : ' + str(dd.strftime("%j"))
print 'Week number of year, Sunday as the first day of week : ' + str(dd.strftime("%U"))
print 'Week number of year, Monday as the first day of week : ' + str(dd.strftime("%W"))
print 'Local version of datetime : ' + str(dd.strftime("%c"))
print 'Local version of time : ' + str(dd.strftime("%X"))
print 'Local version of date : ' + str(dd.strftime("%x"))
print 'A percent character : ' + str(dd.strftime("%%"))

print '-------------- time delta --------------------'

d1=dt.datetime(2020, 5, 17 , 11, 53)
d2=dt.datetime(2022, 11, 12 , 22, 23)
print d2-d1