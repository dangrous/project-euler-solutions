import math

def sum_digits(number):
	string = str(number)
	digits = len(string)
	sum = 0
	for x in range(0,digits):
		sum += int(string[x])
	return sum

if __name__ == "__main__":
	test = pow(2,1000)
	print sum_digits(test)