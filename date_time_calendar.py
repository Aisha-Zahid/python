# ---------------------- Task-1 ----------------------------
import random  # importing module
import time
from datetime import date , time , datetime
  
# calling the today
# function of date class
today = date.today()
now = datetime.now()  
print("Today's date is", today)
print("\nCurrent Date and time is ", now)

print("\nDate components", today.year, today.month, today.day)

# ---------------------- Task-2 ----------------------------
import random
import time

def getRandomDate(startDate, endDate):
    print("Printing random date between", startDate, "and", endDate)

    randomGenerator = random.random()
    dateFormat = '%m/%d/%Y'

    startTime = time.mktime(time.strptime(startDate, dateFormat))
    endTime = time.mktime(time.strptime(endDate, dateFormat))

    randomTime = startTime + randomGenerator * (endTime - startTime)

    randomDate = time.strftime(dateFormat, time.localtime(randomTime))

    return randomDate

print("Random Date =", getRandomDate("1/1/2026", "12/12/2027"))


#---------------------- Task-3 ----------------------------
# Define a function called hotel_cost with one argument nights as input.
def hotel_cost(nights):
    return 140*nights

# Define a function called plane_ride_cost that takes a string, city, as input.

def plane_ride_cost(city):
    if "Charlotte" == city:
        return 183
    elif "Tampa" == city:
        return 220
    elif "Pittsburgh" == city:
        return 222
    elif "Los Angeles" == city:
        return 475

# Define a function called rental_car_cost with an argument called days

def rental_car_cost(days):
    if days >= 7:
        return 40*days - 50
    elif days >= 3:
        return 40*days - 20
    else:
        return 40*days

# Define a function called trip cost with argument day, money and city

def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money

print("Cost of car rental: ", rental_car_cost(5))

print("Cost of plane ride: ", plane_ride_cost("Los Angeles"))

print("Cost of hotel room: ", hotel_cost(7))
print("Total cost of the trip:", trip_cost("Los Angeles", 7, 500))
print(trip_cost("Tampa", 6,500))

#---------------------------------- ACP ----------------------------------
import calendar
import datetime

# Display all month names
for month in range(1, 13):
    print(calendar.month_name[month])