#---------------------- Task-1 ----------------------------
try:
    number = int(input("Enter a number: "))
    print("The number entered is", number)
#using value error 
except ValueError as ex:
    print("Exception:", ex)
    
#---------------------- Task-2 ----------------------------
try:
    num1, num2 = eval(input("Enter two numbers, separated by a comma : "))
    result = num1 / num2
    print("Result is", result)
#using multiple except block for different type of error

except ZeroDivisionError:
    print("Division by zero is error !!")
except SyntaxError:
    print("Comma is missing. Enter numbers separated by comma like this 1, 2")
except:
    print("Wrong input")
else:
    print("No exceptions")
finally:
    print("This will execute no matter what")


# ---------------------- Task-3 ----------------------------
valid = False
while not valid:  
  try:
    n = int(input("Enter a number: "))
    # enter a even number
    while n % 2 == 0:

      print("bye")
    valid = True
  except ValueError:
    print("Invalid")
