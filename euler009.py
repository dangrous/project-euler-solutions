def so_slow(number):
	for x in range(1,number - 1):
		for y in range(1, number - 1):
			for z in range(1, number - 1):
				if x + y + z == number:
					if x*x + y*y == z*z or x*x + z*z == y*y or y*y + z*z == x*x:
						return x * y * z
	return "No triplet found"

if __name__ == "__main__":
	test = input("What is the sum of your triplet? ")
	print so_slow(test)