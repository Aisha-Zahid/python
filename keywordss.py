# ------------------------------- Task-1 -------------------------------
a = input("Enter a word: ")
# program to check break keyword
for i in a:  
  if (i == 'A'):  
    print("A is found")
    break  
  else:

    print("A not found")

# ------------------------------- Task-2 -------------------------------
for x in range(10): 
    if x % 20 == 0:  # condition 1
       print("twist")

    elif x % 15 == 0:  # condition 2
       pass  # pass statement

    elif x % 5 == 0:  # condition 3
       print("fizz")  # display result

    elif x % 3 == 0:  # condition 4
       print("buzz")  # display result

    else:  # condition 5
       print(x)  # display result
       
# ------------------------------- Task-3 -------------------------------
var = 10  
while var > 0:  
   var = var - 1
   if var == 5:  
      continue 
   print('\nCurrent variable value :', var)
print("\nGood bye!")


#------------------------------- Task-4 -------------------------------
# Program to calculate customer due amount

# taking input from user
bill_amount = float(input("Enter total bill amount: "))
paid_amount = float(input("Enter paid amount: "))

# calculating due
due_amount = bill_amount - paid_amount

# checking condition
if due_amount > 0:
    print("Customer still has to pay:", due_amount)
elif due_amount == 0:
    print("No due. Bill is fully paid.")
else:
    print("Extra amount paid:", abs(due_amount))
