#------------------------------- Task-1 -------------------------------
print("Half Pyramid Pattern of Stars (*):")
n = int(input("enter the number of rows: "))
# outer loop to handle number of rows
for i in range(n):
  # inner loop to handle number of columns
    for j in range(i+1):
        print("* ", end="")
    print()

# ------------------------------- Task-2 -------------------------------
rows = int(input("Please Enter the total Number of Rows  : "))
number = 1  
print("Floyd's Triangle")

for i in range(1, rows + 1):
  
    for j in range(1, i + 1):
        print(number, end='  ')
        number = number + 1
    print()

# ------------------------------- Task-3 -------------------------------
n = int(input("Enter size: "))

# Upper part
for i in range(1, n+1):
    print(" " * (n - i), end="")   # spaces
    for j in range(1, 2*i):
        print(j, end="")           # numbers
    print()

# Lower part
for i in range(n-1, 0, -1):
    print(" " * (n - i), end="")   # spaces
    for j in range(1, 2*i):
        print(j, end="")           # numbers
    print()
