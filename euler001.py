def sum_3mults_and_5mults(maxInt):
	sum = 0
	for x in range(1, maxInt):
		if x % 3 == 0 or x % 5 == 0:
			sum += x
	return sum

if __name__ == "__main__":
	maxInt = input("Please enter the maximum number you wish to sum: ")
	print sum_3mults_and_5mults(maxInt)