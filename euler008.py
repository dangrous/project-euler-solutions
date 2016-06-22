def largest_product_in_series(digits, number):
	length = len(number);
	tracker = 0
	max_product = 0
	while tracker < length - digits:
		test_product = 1
		# skip to next set if there are any zeros? For efficiency
		for x in range(0,digits):
			test_product *= int(number[tracker + x])
		if test_product > max_product:
			max_product = test_product
		tracker += 1
	return max_product

if __name__ == "__main__":
	digits = input("How many adjacent digits? ")
	number = raw_input("Please enter the number to search: ")
	print largest_product_in_series(digits, number)