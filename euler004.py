def find_palindrome(digits):
	maxPal = 0
	maxNumber = ""
	for x in range(0, digits):
		maxNumber += "9"
	minNumber = 0
	if digits != 1:
		minNumber = int(maxNumber[1:])

	for x in range(int(maxNumber),minNumber, -1):
		for y in range(x,minNumber, -1):
			total = x * y
			totalString = str(total)
			palindrome = True
			for z in range(0,len(totalString)):
				if totalString[z] != totalString[-(z+1)]:
					palindrome = False
					break
			if palindrome and total > maxPal:
				maxPal = total

	return maxPal

if __name__ == "__main__":
	digits = input("How many digits in the initial two numbers? ")
	print find_palindrome(digits)
