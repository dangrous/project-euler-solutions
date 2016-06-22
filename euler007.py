import math

def find_prime(number):
	prime_tracker = 0
	test_number = 2
	while prime_tracker < number:
		if is_prime(test_number):
			prime_tracker += 1
		test_number += 1
	return test_number - 1

def is_prime(number):
	x = 2
	sqrt = math.sqrt(number)
	while x <= sqrt:
		if number % x == 0:
			return False
		x += 1
	return True

if __name__ == "__main__":
	test = input("What nth prime would you like to find? ")
	print find_prime(test)