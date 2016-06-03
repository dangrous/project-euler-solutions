def find_palindrome():
	maxPal = 0
	for x in range(999,99, -1):
		for y in range(x,99, -1):
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
	print find_palindrome()
