# save all results to save a huge amount of time (50 s down to 3.5 s)
collatz_nums = {}

def find_longest_collatz(number):
	longest = 1
	start = 1
	for x in range(1, number):
		collatz_nums[x] = collatz_steps(x)
		if collatz_nums[x] >= longest:
			start = x
			longest = collatz_nums[x]
	return start

def collatz_steps(number):
	steps = 0
	if number == 1:
		steps += 1
	# massively cuts down on the steps
	elif number in collatz_nums:
		steps += collatz_nums[number]
	elif number % 2 == 0:
		steps += 1 + collatz_steps(number / 2)
	else:
		steps += 1 + collatz_steps(3 * number + 1)
	return steps

if __name__ == "__main__":
	test = input("What's the highest starting number you want? ")
	print find_longest_collatz(test)