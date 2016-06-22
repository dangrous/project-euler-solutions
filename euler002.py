def sum_even_fibs(maxInt):
	lastVal = 1
	currentVal = 2
	sum = 0
	while currentVal < maxInt:
		if currentVal % 2 == 0:
			sum += currentVal
		lastVal, currentVal = currentVal, lastVal + currentVal
	return sum

if __name__ == "__main__":
	maxInt = input("Please enter the maximum number you wish to sum to: ")
	print sum_even_fibs(maxInt)