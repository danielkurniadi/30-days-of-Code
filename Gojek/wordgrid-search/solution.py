from itertools import product
import sys

def solve(input_path, output_path):
	"""Solution handler
	"""
	dirs = [
		(-1, -1), # left, up
		(-1, 1), # left, down
		(-1, 0), # left straight
		(0, -1), # up straight
		(0, 1), # down straight
		(1, -1), # right up
		(1, 0), # right straight
		(1, 1), # right down
	]
	
	f = open(input_path, "r")
	T = int(f.readline())
	solutions = []
	for _ in range(T):
		N = int(f.readline())
		M = int(f.readline())
		grid = load_grid(f, N)
		word = str(f.readline()).strip()
		#print("WORD",word)
		s = 0
		#print(grid)
		for i, j, direction in product(range(N), range(M), dirs):
			#print(i, j, direction)
			extracted = extract(grid, i, j, len(word), direction)
			if (extracted) and (extracted == word):
				#print(extracted)
				s += 1
		solutions.append(s)
	f.close()
	output_pretty(output_path, solutions)

def output_pretty(outpath, solutions):
	"""Format output and save in .txt file
	"""
	f = open(outpath, "w")
	for idx, s in enumerate(solutions):
		f.write("Case {}: {}\n".format(idx+1, s))
	f.close()

def load_grid(f, n):
	"""Load grid of words into 2D char array/ list of string
	"""
	grid = []
	for _ in range(n):
		grid.append(str(f.readline()).strip())
	return grid
			
def extract(grid, i, j, length, dirr):
	"""Extract words in given dir from the grid
	"""
	#print(dirr[0], dirr[1])
	if ((0 <= (i + (length-1) * dirr[0]) < len(grid)) and
	(0 <= (j + (length-1) * dirr[1]) < len(grid[0]))):
		return "".join([grid[i + k*dirr[0]][j + k*dirr[1]] for k in range(length)])
	return None

if __name__ == '__main__':
	solve("input.txt", "output.txt")
