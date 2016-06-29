# this one's a little more complicated, adding in File I/O
import time
# declaring the global variable
grid = []

def read_grid(filename):
	with open(filename) as f:
		lines = f.readlines()
		for line in lines:
			trav = 0
			line_nums = []
			while trav < len(line):
				if line[trav].isdigit():
					line_nums.append(int(line[trav:trav+2]))
					trav += 2
				else:
					trav += 1
			grid.append(line_nums)

def test_grid(grid):
	start_time = time.time()
	greatest = 0
	# storing this and len(line) makes it slightly faster
	len_grid = len(grid)
	for grid_index, line in enumerate(grid):
		len_line = len(line)
		for index, number in enumerate(line):
			if len_line >= index + 4:
				hor_prod = line[index] * line[index + 1] * line[index + 2] * line[index + 3]
				if hor_prod > greatest:
					greatest = hor_prod
			if len_grid >= grid_index + 4:
				vert_prod = grid[grid_index][index] * grid[grid_index + 1][index] * grid[grid_index + 2][index] * grid[grid_index + 3][index]
				if vert_prod > greatest:
					greatest = vert_prod
			if len_grid >= grid_index + 4 and len_line >= index + 4:
				rdiag_prod = grid[grid_index][index] * grid[grid_index + 1][index + 1] * grid[grid_index + 2][index + 2] * grid[grid_index + 3][index + 3]
				if rdiag_prod > greatest:
					greatest = rdiag_prod
			if len_grid >= grid_index + 4 and index >= 3:
				ldiag_prod = grid[grid_index][index] * grid[grid_index + 1][index - 1] * grid[grid_index + 2][index - 2] * grid[grid_index + 3][index - 3]
				if ldiag_prod > greatest:
					greatest = ldiag_prod
	print("--- %s seconds ---" % (time.time() - start_time))
	return greatest

if __name__ == "__main__":
	filename = raw_input("Please enter the name of the grid file: ")
	read_grid(filename)
	print test_grid(grid)