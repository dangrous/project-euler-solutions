def sum_square_difference(number):
	return square_sum(number) - sum_square(number)

def square_sum(number):
	sum = 0
	for x in range(1, number + 1):
		sum += x
	return sum * sum

def sum_square(number):
	sum = 0
	for x in range(1, number + 1):
		sum += x*x
	return sum

if __name__ == "__main__":
	test = input("How many natural numbers? ")
	print sum_square_difference(test)