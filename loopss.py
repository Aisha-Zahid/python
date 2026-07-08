num = 17
print("Table of 17")
for i in range(1,11):
  mul = num*i
  print("17 x %d = %d" % (i, mul))


#-------------------------------------- while loooppp----------------
num = 1
sum = 0
while (num <= 10):
  sum = sum+num
  num = num+1

print("Sum of First 10 Natural Numbers :", sum)



#---------------- acp-------------------
n = int(input("Enter number of terms: "))
m= int(input("Enter number of terms: "))
for i in range(1, n + 1):
    print(i ** m, end=" ")