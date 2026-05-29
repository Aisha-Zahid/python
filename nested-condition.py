#---------------------------------- Task 1 --------------------------------
medical_cause = input("Did you have a medical cause? (Y/N): ").strip().upper()

if medical_cause == 'Y':   
    print("You are allowed")
else:
    atten = int(input("Enter the attendance of the student: "))

    if atten >= 75:  
        print("Allowed")
    else:
        print("Not allowed")


# ---------------------------------- Task 2 --------------------------------
units = int(input("Enter units: "))

bill = 0

if units <= 50:
    bill = units * 2.60 + 25

elif units <= 100:
    bill = (50 * 2.60) + (units - 50) * 3.25 + 35

elif units <= 200:
    bill = (50 * 2.60) + (50 * 3.25) + (units - 100) * 5.26 + 45

else:
    bill = (50 * 2.60) + (50 * 3.25) + (100 * 5.26) + (units - 200) * 8.45 + 75

print("Total Bill =", round(bill, 2))


# ---------------------------------- Task 3 --------------------------------
print("Select your ride: ")
print("1. Bike")
print("2. Car")
choice = int(input("Enter your choice: "))
if (choice == 1):
  print("what type of bike? ")
  print("1.Scooty\n")
  print("2.Scooter\n")
  choice2 = int(input("Enter you choice2: "))
  if choice2 == 1:  
    print("you have selected scooty")
  else:
    print("you have selected scooter")
elif (choice == 2):  
  print("what type of car?")
  print("1.Sedan")
  print("2.XUV")
  choice3 = int(input("enter your choice3: "))

  if choice3 == 1:  
      
    print("you have selected sedan")
  else:
    print("you have selected XUV")
else:  
  print("Wrong choice!")
