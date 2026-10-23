from datetime import datetime as dandt, timedelta as td
from datetime import date as dt

def divisorLine():
    print("----------------------------------------------------------------")

# 1)Print Current Date and Time
print("1)Current Date and Time is: {}".format(dandt.now()))
divisorLine()

# 2)Print Current Date only
print("2)Current Date only is: {}".format(dt.today()))
divisorLine()

# 3)Print Current Date in DD-MM-YYYY format
print("3)Current Date in DD-MM-YYYY format is: {}".format(dandt.now().strftime("%d-%m-%Y")))
divisorLine()

# 4)Convert String into datetime
stringToDateTimeOne = "06-04-1986 04:45:56 AM"
print("4)After converted String {} into datetime object is: {}".format(stringToDateTimeOne, dandt.strptime(stringToDateTimeOne, "%d-%m-%Y %H:%M:%S %p")))
divisorLine()

# 5)Find difference between two dates
dateOfBirth = dandt(1986,4,6)
currentDate = dandt(2026,9,5)

dateDifference = currentDate - dateOfBirth
print("5)Difference dates between {} and {} in dates format is: {}".format(dateOfBirth, currentDate, dateDifference))
print("5)Difference dates between {} and {} in days format is: {}".format(dateOfBirth, currentDate, dateDifference.days))
divisorLine()

# 6)Calculate age from date of birth
kiranKumarDateOfBirth = "06-04-1986 12:12:24 AM"
age = dt.today().year - dandt.strptime(kiranKumarDateOfBirth, "%d-%m-%Y %I:%M:%S %p").year
if (dt.today().day, dt.today().month) < (dandt.strptime(kiranKumarDateOfBirth, "%d-%m-%Y %I:%M:%S %p").day,
                                         dandt.strptime(kiranKumarDateOfBirth, "%d-%m-%Y %I:%M:%S %p").month):
    age -= 1
print("6)Kiran Kumar age is: {} years".format(dateDifference.days/365))
divisorLine()

# 7)Add 40 days to current date.
currentDateAdd = dt.today()
print("7)Current Date is: {}".format(currentDateAdd))
print("7)Date after 40 days is: {}".format(currentDateAdd + td(40)))
divisorLine()

# 8) Subtract 40 days to current date
currentDateSub = dt.today()
print("8)Current date is: {}".format(currentDateSub))
print("8)Date before currentDate of 40 days is: {}".format(currentDateSub - td(40)))
divisorLine()

# 9)Find date after one year
currentDateAfterOneYear = dt.today()
print("9)Current date is: {}".format(currentDateAfterOneYear))
print("9)Date after one year is: {}".format(currentDateAfterOneYear.replace(currentDateAfterOneYear.year+1)))
divisorLine()

# 10)Check is the year is leap year or not
import calendar
checkLeapYear = dt.today().year
print("10){} is leap year? {}".format(checkLeapYear, calendar.isleap(checkLeapYear)))
divisorLine()

# 11)Find day of the week
enterDate = dt(2026,9,7)
print("11)Current date is: {} and weekday is: {}".format(enterDate, enterDate.strftime("%A")))
print("11)Current date is: {} and weekday is: {} through calendar.weekday".format(enterDate, calendar.weekday(enterDate.year, enterDate.month, enterDate.day)))
# *** calendar.weekday returns an integer from 0 to 6, where 0 is Monday and 6 is Sunday.****
divisorLine()

# 12)Find number of days between two dates
firstDate = dt(1986,4,6)
secondDate = dt(1986,4,4)
differenceDateInDays = (firstDate - secondDate).days
print("12)Number of days different between {} and {} is: {} days".format(secondDate,firstDate,differenceDateInDays))
divisorLine()

# 13)Check Given Date is Today or not.
dateInput = dt(2026,10,2)
print("13) Entered date is: {}".format(dateInput))
if dateInput == dt.today():
    print("13) {} is today!".format(dateInput))
else:
	print("13) {} is not today!".format(dateInput))
divisorLine()

# 14)Compare Two Dates
firstDateInput = dt(1986,4,6)
secondDateInput = dt(1994,8,11)
print("14) Entered first date and second dates are: {} {} respectively".format(firstDateInput, secondDateInput))
if firstDateInput > secondDateInput:
	print("14) {} is earlier to {}.".format(firstDateInput, secondDateInput))
elif firstDateInput < secondDateInput:
	print("14) {} is later to {}.".format(firstDateInput, secondDateInput))
else:
	print("14) Both {} and {} are same.".format(firstDateInput, secondDateInput))
divisorLine()

# 15)Find Last day of the month
presentYear = 2026
presentMonth = 9
print("15)Last date of the month {} of year {} is: {} and day is: {}.".format(presentMonth, presentYear,
      calendar.monthrange(presentYear, presentMonth)[1], dt(presentYear, presentMonth, calendar.monthrange(presentYear, presentMonth)[1]).strftime("%A")))
divisorLine()

# 16)Find First and Second date and respective day
inputYear = 1986
inputMonth = 8
print("#16) Entered Year and Month are: {}, {} respectively!".format(inputYear, inputMonth))
firstDay = dt(inputYear, inputMonth, 1).strftime("%A")
lastDay = dt(inputYear, inputMonth, calendar.monthrange(inputYear, inputMonth)[1]).strftime("%A")
print("First date is: {} and day is: {} and Last date is: {} and last day is: {}"
      .format(dt(inputYear, inputMonth, 1), firstDay, dt(inputYear, inputMonth, calendar.monthrange(inputYear, inputMonth)[1]), lastDay))
divisorLine()

#17)Find number of days in a Month
findNoOfDaysInMonthYear = 2026
findNoOfDaysInMonthMonth = 12
print("17)Number of days in given year {} and month {} is: {}.".format(findNoOfDaysInMonthYear, findNoOfDaysInMonthMonth, calendar.monthrange(findNoOfDaysInMonthYear, findNoOfDaysInMonthMonth)[1]))
divisorLine()

#18)Find whether a date is weekend or not
enterDateToFindWeekendOrWeekday = dt(2026,9,14)
if calendar.weekday(enterDateToFindWeekendOrWeekday.year, enterDateToFindWeekendOrWeekday.month, enterDateToFindWeekendOrWeekday.day) >= 5:
	print("18)Entered date is: {}, day is: {} and it is weekend!".format(enterDateToFindWeekendOrWeekday,enterDateToFindWeekendOrWeekday.strftime("%A")))
else:
	print("18)Entered date is: {}, day is: {} and it is not weekend!".format(enterDateToFindWeekendOrWeekday,enterDateToFindWeekendOrWeekday.strftime("%A")))
divisorLine()

#19)Convert one date format into another date format
enterDateToConvert = "06-04-1986 20:40:20 PM"
inputDateIs = dandt.strptime(enterDateToConvert, "%d-%m-%Y %H:%M:%S %p")
print("Input date is: {}.".format(inputDateIs))
convertFormat = inputDateIs.strftime("%d/%m/%Y %H:%M:%S %p")
print("After convertion input date is: {}.".format(convertFormat))
divisorLine()

#20)Find number of hours between two datetime objects
fDandT = dandt(2026,9,7,4,30,20)
sDandT = dandt(2026,9,8,8,30,20)
dDandT = sDandT - fDandT
dDandTHours = dDandT.total_seconds() / 3600
print("20)Number of hours between {} and {} is: {} hours.".format(fDandT,sDandT,dDandTHours))
divisorLine()










