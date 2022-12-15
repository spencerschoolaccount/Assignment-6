try:
	iterations = int(input('How many iterations would you like?\n'))
except:
	exit("Invalid input")
a = 1
pi = 0
for i in range(0,iterations):
	if i % 2 == 0:
		pi += 4/a
	else:
		pi -= 4/a
	a += 2
	print("\nCurrent divisor: " + str(a))
	print(pi)