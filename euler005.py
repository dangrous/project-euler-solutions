def find_smallest_multiple(number):
	factors = []
	for x in range(number,1,-1):
		factors = add_new_factors(x,factors)
	small_mult = 1
	for factor in factors:
		small_mult *= factor
	return small_mult

def add_new_factors(number, factors):
	new_factors = []
	for x in range (2,number+1):
		if number % x == 0 and is_prime(x):
			new_factors.append(x)
			if power_of_(x,number):
				for y in range(1, power_of_(x,number)):
					new_factors.append(x)
	for factor in new_factors:
		while factors.count(factor) < new_factors.count(factor):
			factors.append(factor)
	return factors

def power_of_(x, goal):
	tracker = 0
	while x**tracker < goal:
		tracker += 1
		if x**tracker == goal:
			return tracker
	return 0

def is_prime(number):
	x = 2
	while x <= number / 2:
		if number % x == 0:
			return False
		x += 1
	return True

if __name__ == "__main__":
	test = input("What's the highest factor you want? ")
	print find_smallest_multiple(test)
