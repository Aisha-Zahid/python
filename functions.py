# ------------------------------- Task-1 -------------------------------
def well_wishes():
  print("hello")
  print("how are you?")

well_wishes()


# ------------------------------- Task-2 -------------------------------
def weather_condition():
  print('The weather is pleasant in:', spring)
  print('The weather is same in', autumn)

spring = "autumn"
autumn = spring
weather_condition()


# ------------------------------- Task-3 -------------------------------
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

print("a) Add  b) Subtract  c) Multiply  d) Divide")

choice = input("Enter choice: ")
x = int(input("First number: "))
y = int(input("Second number: "))

if choice == 'a':
    print(add(x, y))

elif choice == 'b':
    print(sub(x, y))

elif choice == 'c':
    print(mul(x, y))

elif choice == 'd':
    print(div(x, y))

else:
    print("Invalid input")


#-------------------------------- ACP--------------------------
def circumference(r):
    return 2 * 3.14 * r

print(circumference(5))