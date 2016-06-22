import math

def sum_primes(number):
	test_number = 2
	sum = 0
	while test_number < number:
		if is_prime(test_number):
			sum += test_number
		test_number += 1
	return sum

def is_prime(number):
	x = 2
	sqrt = math.sqrt(number)
	while x <= sqrt:
		if number % x == 0:
			return False
		x += 1
	return True

if __name__ == "__main__":
	test = input("What is the max prime number you wish to sum? ")
	print sum_primes(test)