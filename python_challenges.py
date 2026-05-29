#------------------------------- Task 1 -------------------------------
# Operator Precedence
v = 4
w = 5
x = 8
y = 2
z = 0

z = (v + w) * x / y

print("Value of (v+w) * x / y is : ", z)





# ------------------------------- Task 2 -------------------------------
# Divisible Number
print("Enter a Number (Numerator): ")
numn = int(input())

print("Enter a Number (Denominator): ")
numd = int(input())

if numn % numd == 0:
    print(numn, "is divisible by", numd)
else:
    print(numn, "is not divisible by", numd)

#-------------------------------- Task 3 -------------------------------
# Mean Value
mean1 = 38
wrong_number = 36
correct_number = 56
total_number = 40

sum = mean1 * total_number
print(sum)

sum = sum - wrong_number + correct_number
print(sum)

mean2 = sum / total_number
print(mean2)


#------------------------------------- Task 4 -----------------------------
a = int(input("enter a value: "))
b = int(input("enter value 2 :"))
c = int(input("enter value 3: "))

avg = (a + b + c) / 3
print("avg =", avg)

if avg > a and avg > b and avg > c:
    print("%d is higher than %d, %d, %d" % (avg, a, b, c))
elif avg > a and avg > b:
    print("%d is higher than %d, %d" % (avg, a, b))
elif avg > a and avg > c:
    print("%d is higher than %d, %d" % (avg, a, c))
elif avg > b and avg > c:
    print("%d is higher than %d, %d" % (avg, b, c))
elif avg > a:
    print("%d is just higher than %d" % (avg, a))
elif avg > b:
    print("%d is just higher than %d" % (avg, b))
elif avg > c:
    print("%d is just higher than %d" % (avg, c))
else:
  print("invalid input")
