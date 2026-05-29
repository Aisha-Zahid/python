# Let's check the datatype of different values
a = 5
print("type of a: ", type(a))

b = 2.5
print("type of b: ", type(b))

c = "coding"
print("type of c: ", type(c))

d = True
print("type of d: ", type(d))


# input a word
text = str(input("Enter a string: "))

# Reverse String
# using step value as -1 to iterate in reverse
revText = text[::-1]
text = revText

print("Reverse of Given String is:")
print(text)
