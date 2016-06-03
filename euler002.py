def sum_even_fibs():
	lastVal = 1
	currentVal = 2
	sum = 0
	maxInt = input("Please enter the maximum number you wish to sum to: ")
	while currentVal < maxInt:
		if currentVal % 2 == 0:
			sum += currentVal
		lastVal, currentVal = currentVal, lastVal + currentVal
	return sum

if __name__ == "__main__":
	print sum_even_fibs()