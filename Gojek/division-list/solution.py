import numpy as np

def solve(input_path):
	f = open(input_path, "r")
	n = int(f.readline())
	solutions = []
	for _ in range(n):
		a = int(f.readline())
		b = int(f.readline())
		k = int(f.readline())
		numarr = np.arange(a, b+1)
		s = np.sum(numarr%k == 0)
		solutions.append(s)
	f.close()
	output_pretty("output.txt", solutions)

def output_pretty(output_path, solutions):
	f = open(output_path, "w")
	for i, s in enumerate(solutions):
		f.write("Case {}: {}\n".format(i+1, s))
	f.close()
if __name__ == '__main__':
	solve("input.txt")
