# establishing base cases - probably there's a better way to do this?
ones = [4, 3, 3, 5, 4, 4, 3, 5, 5, 4] # zero, one, two, three, four, five, six, seven, eight, nine
teens = [3, 6, 6, 8, 8, 7, 7, 9, 8, 8] # ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen
tens = [3, 6, 6, 5, 5, 5, 7, 6, 6] # ten, twenty, thirty, forty, fifty, sixty, seventy, eighty, ninety
powers = [7, 8] # hundred, thousand

# storing an array like in 016
sums = {}

def count_all_letters(number):
	digit_sum = 0
	for x in range(1, number + 1):
		digit_sum += count_letters(x)
	return digit_sum

# a little unnecessary abstraction here but will eventually be able to expand out to bigger numbers
def count_letters(number):
	digit_sum = 0
	number_string = str(number)
	digit_count = len(number_string)
	if number == 0:
		return digit_sum
	# nice speed upgrade here, at least for low level numbers
	elif number in sums:
		digit_sum += sums[number]
	elif digit_count == 1:
		digit_sum += ones[number % 10]
	elif digit_count == 2:
		if number_string[0] == '1':
			digit_sum += teens[number % 10]
		else:
			digit_sum += tens[number / 10 - 1]
			digit_sum += count_letters(number % 10)
	else:
		digit_sum += ones[number / pow(10,digit_count - 1)] + powers[digit_count - 3]
		if number % pow(10,digit_count - 1) != 0:
			if digit_count == 3:
				digit_sum += 3
			digit_sum += count_letters(number % pow(10,digit_count - 1))
	sums[number] = digit_sum
	return digit_sum


if __name__ == "__main__":
	test = input("What's the highest number you want to sum? ")
	print count_all_letters(test)