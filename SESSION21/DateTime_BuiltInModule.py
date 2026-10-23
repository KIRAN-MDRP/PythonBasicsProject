# This program illustrates the methods and features of DateTime Built-in Module.
# import datetime as dt
from datetime import datetime as dt, timezone as tz
from zoneinfo import ZoneInfo

# print("Date time built-in modules members and features are: {}.".format(dir(datetime)))

#Current Date and Time is:
print("Current Date and Time is: {}".format(dt.now()))
print("Current Date and Time in Standard Foramt is: {}".format(dt.now().strftime("%Y-%m-%d %H:%M:%S %p")))
print("Only Time is: {}".format(dt.now().time().strftime("%H:%M:%S")))
print("Only Date is: {}".format(dt.now().date().strftime("%d-%m-%y")))
print("Only Year is: {}".format(dt.now().year))
print("Only Day is: {}".format(dt.now().strftime("%A")))
print("Only Month is: {}".format(dt.now().strftime("%B")))
print("Only Weekday is: {}".format(dt.now().strftime("%w")))
print("Only Weekday is: {}".format(dt.now().strftime("%W")))
print("Only Weekday is: {}".format(dt.now().strftime("%U")))
print("Only Weekday is: {}".format(dt.now().strftime("%u")))

# We have 40 methods are there associated with datetime module.
# 1)astimezone 2)combine 3)ctime 4)date 5)day 6)dst



# 1)astimezone() - Used to convert time from one time zone to another time zone.
currentUTCTime = dt.now(tz.utc)
print("Current UTC Time is: {}".format(currentUTCTime))
# istTimezone = currentUTCTime.astimezone(ZoneInfo('Asia/Tokyo')).strftime("%Y-%m-%d %H:%M:%S %p")
# print("Current IST Time is: {}".format(istTimezone))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 2)combine() - Used to combine date and time into a single datetime object.
# meetingDate = dt.date('2026, 8, 15')
# meetingTime = dt.time(10, 30, 0)
# meetingDateTime = dt.combine(meetingDate, meetingTime)
# print("Meeting Date and Time is: {}".format(meetingDateTime))
# print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 3)ctime() - Used to return the current date and time in a string format.
print("Current Date and Time is: {}".format(dt.ctime(dt.now())))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 4)date() - Used to return the date object.
print("Current Date is: {}".format(dt.now().date()))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 5)day() - Used to return the day of the week as an integer.
print("Current Day is: {}".format(dt.now().day))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 6)dst() - Used to return the daylight saving time offset in minutes.
print("Current Daylight Saving Time Offset is: {}".format(dt.now().dst()))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 7)fold - Used to return the fold attribute of the datetime object.
print("Current Fold is: {}".format(dt.now().fold))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 8)fromisocalendar() - Used to return a datetime object from the ISO calendar date.
print("Current Date and Time is: {}".format(dt.fromisocalendar(2026, 8, 6)))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 9)fromordinal() - Used to return a datetime object from the ordinal date.
print("Current Date and Time is: {}".format(dt.fromordinal(738624)))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 10)fromisoformat() - Used to return a datetime object from the ISO format string.
print("Current Date and Time is: {}".format(dt.fromisoformat("2026-08-15")))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 11)fromtimestamp() - Used to return a datetime object from the timestamp.
print("Current Date and Time is: {}".format(dt.fromtimestamp(1692000000)))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 12)hour() - Used to return the hour of the datetime object.
print("Current Hour is: {}".format(dt.now().hour))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 13)isocalendar() - Used to return a tuple containing the ISO calendar date.
print("Current ISO Calendar Date is: {}".format(dt.now().isocalendar()))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 14)isoformat() - Used to return a string representing the date and time in ISO 8601 format.
print("Current Date and Time in ISO Format is: {}".format(dt.now().isoformat()))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 15)isoweekday() - Used to return the day of the week as an integer, where Monday is 1 and Sunday is 7.
print("Current Day of the Week is: {}".format(dt.now().isoweekday()))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 16)max() - Used to return the latest possible date and time.
print("Latest Possible Date and Time is: {}".format(dt.max))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 17)min() - Used to return the earliest possible date and time.
print("Earliest Possible Date and Time is: {}".format(dt.min))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 18)minute() - Used to return the minute of the datetime object.
print("Current Minute is: {}".format(dt.now().minute))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 19)month() - Used to return the month of the datetime object.
print("Current Month is: {}".format(dt.now().month))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 20)replace() - Used to return a new datetime object with the specified values replaced.
print("Current Date and Time with replaced values is: {}".format(dt.now().replace(year=2023, month=10, day=15, hour=12, minute=30, second=45)))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 21)resolution - Used to return the smallest possible difference between two datetime objects.
print("Smallest Possible Difference between two datetime objects is: {}".format(dt.resolution))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 22)second() - Used to return the second of the datetime object.
print("Current Second is: {}".format(dt.now().second))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 23)striptime() - Used to return a datetime object from a string representing a date and time.
print("Current Date and Time from string is: {}".format(dt.strptime("2023-10-15 12:30:45", "%Y-%m-%d %H:%M:%S")))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 24)time() - Used to return the time of the datetime object.
print("Current Time is: {}".format(dt.now().time()))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 25)timestamp() - Used to return the timestamp of the datetime object.
print("Current Timestamp is: {}".format(dt.now().timestamp()))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 26)timetuple() - Used to return the time of the datetime object as a tuple.
print("Current Time as Tuple is: {}".format(dt.now().timetuple()))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 27)timetz() - Used to return the time of the datetime object as a time object.
print("Current Time as Time Object is: {}".format(dt.now().timetz()))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 28)today() - Used to return the current date and time.
print("Current Date and Time is: {}".format(dt.now().today()))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 29)toordinal() - Used to return the ordinal of the datetime object.
print("Current Date and Time as Ordinal is: {}".format(dt.now().toordinal()))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 30)tzinfo - Used to return the timezone of the datetime object.
print("Current Timezone is: {}".format(dt.now().tzinfo))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 31)tzname() - Used to return the name of the timezone of the datetime object.
print("Current Timezone Name is: {}".format(dt.now().tzname()))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 32)utcfromtimestamp() - Used to return the datetime object from a timestamp.
# print("Current Date and Time from Timestamp is: {}".format(dt.utcfromtimestamp(dt.now().timestamp())))
# print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 33)utcoffset() - Used to return the UTC offset of the datetime object.
print("Current UTC Offset is: {}".format(dt.now().utcoffset()))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 34)utctimetuple() - Used to return the UTC time of the datetime object as a tuple.
print("Current UTC Time as Tuple is: {}".format(dt.now().utctimetuple()))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 35)weekday() - Used to return the weekday of the datetime object.
print("Current Weekday is: {}".format(dt.now().weekday()))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 36)year - Used to return the year of the datetime object.
print("Current Year is: {}".format(dt.now().year))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 37)microsecond() - Used to return the microsecond of the datetime object.
print("Current Microsecond is: {}".format(dt.now().microsecond))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 38)now() - Used to return the current date and time.
print("Current Date and Time is: {}".format(dt.now()))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 39)utcnow() - Used to return the current date and time in UTC.
print("Current Date and Time in UTC is: {}".format(dt.utcnow()))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 40)strftime() - Used to return the date and time in a specified format.
print("Current Date and Time in specified format is: {}".format(dt.now().strftime("%Y-%m-%d %H:%M:%S")))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")



