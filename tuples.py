# ------------------------------- Task-1 -------------------------------
# Create a tuple with different data types
tuplex = ("tuple", False, 3.2, 1)
print(tuplex)
# create a tuple
tuplex = (4, 6, 2, 8, 3, 1)
print(tuplex)

tuplex = tuplex + (9,)
print(tuplex)
# Counts the number of occurrences of item 50 from a tuple
tuple1 = (50, 10, 60, 70, 50)
print(tuple1.count(50))


# ------------------------------- Task-2 -------------------------------
# function to check whether palindrome or not

def palind(r):
	e = len(r) - 1
	s = 0
	while (s < e):
		if (r[s] != r[e]):
			return False
		s += 1
		e -= 1
	return True

r = (1, 2, 3, 3, 2, 1)

if (palind(r)):
	print("The Tuple is Flip-Flop")
else:
	print("The Tuple is not Flip-Flop")


# ------------------------------- Task-3 -------------------------------
weather = (1, 0, 0, 0, 1, 1, 0)
sunny = 0
rainy = 0
for i in range(0, 7):
	if (weather[i] == 0):
		rainy += 1
	else:
		sunny += 1

if (sunny > rainy):
	print("Good weather")
else:
	print("Bad weather")
