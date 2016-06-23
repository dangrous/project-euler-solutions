def target_factors_of_triangle(number):
	factors = 0
	test_number = 0
	while factors < number:
		test_number += 1
		test_triangle = triangle(test_number)
		# This IF makes it a little faster
		# assuming that a non-mult of 2 would never have the most factors
		# Is that true? I don't know.
		if test_triangle % 2 == 0:
			test_factors = count_factors(test_triangle)
			if test_factors > factors:
				factors = test_factors
	return test_triangle

def count_factors(number):
	count = 0
	max = number
	x = 1
	while x < max:
		if number % x == 0:
			count += 2
			max = number / x
			if max == x:
				count -= 1
		x += 1
	return count

def triangle(number):
	# found formula on mathisfun.com
	return number * (number + 1) / 2

if __name__ == "__main__":
	test = input("How many factors are you looking for? ")
	print target_factors_of_triangle(test)