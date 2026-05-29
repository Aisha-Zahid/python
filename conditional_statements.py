#------------------------------- Task 1 -------------------------------
num = 3
if num > 0:
    print(num, "is a positive number.")

num = -1
if num > 0:
    print(num, "is a positive number.")
else:
    print(num, "is a negative number.")

#------------------------------- Task 2 -------------------------------
number = int(input("Enter Number to check"))
print("Number to be checked :", number)

if number % 2 == 0:
  print("This is an even number")

else:
  print("This is an odd number")
  #------------------------------- Task 3 -------------------------------
  
  i = int(input("enter a number : "))
if (i < 15):
    print("i is smaller than 15")
    print("i'm in if Block")
else:
    print("i is greater than 15")
    print("i'm in else Block")
print("i'm not in if and not in else Block")
