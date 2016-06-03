def find_largest_prime_factor(maxInt):
	x = 2
	while x < maxInt / 2:
		if maxInt % x == 0:
			if is_prime(maxInt / x):
				return maxInt / x
		x += 1

def is_prime(number):
	x = 2
	while x < number / 2:
		if number % x == 0:
			return False
		x += 1
	return True

if __name__ == "__main__":
	maxInt = input("Please enter the prime you wish to factor: ")
	print find_largest_prime_factor(maxInt)