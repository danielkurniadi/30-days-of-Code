import string
import sys
sys.setrecursionlimit(35000)
class G: 
	def __init__(self, row, col, gmap): 
		self.ROW = row 
		self.COL = col 
		self.graph = gmap
		self.tribeset, self.conflicts = {}, 0
  
	def isSafe(self, i, j, visited): 
		""" A helper function to check if cell 
		can be included for DFS operation.
		"""
		return ((0 <= i < self.ROW) and 
				(0 <= j < self.COL) and 
				not (visited[i][j]) and (self.graph[i][j] != '#'))
	
	def isConflict(self, i, j, tribe):
		""" A helper function to check if 
		there is a conflict in the region.
		"""
		return ((self.graph[i][j] in string.ascii_lowercase) and
				(self.graph[i][j] != tribe))

	def DFS(self, i, j, visited, tribe): 
		""" A helper function to do DFS for a 2D 
		boolean matrix. 
		"""
		dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]

		visited[i][j], is_conflict = True, False
		
		if self.isConflict(i, j, tribe):
			self.conflicts += 1
			is_conflict = True

		for k in range(4):
			if self.isSafe(i + dirs[k][0], j + dirs[k][1], visited):
				conf = self.DFS(i + dirs[k][0], j + dirs[k][1], visited, tribe)
				is_conflict = True if conf else is_conflict
		return is_conflict

	def countTribes(self): 
		"""Count number of tribe.
		"""
		visited = [[False for j in range(self.COL)] for i in range(self.ROW)] 

		for i in range(self.ROW): 
			for j in range(self.COL):
				point = self.graph[i][j]

				if (visited[i][j] == False) and (point in string.ascii_lowercase):
					conf = self.DFS(i, j, visited, point)
					if not conf:
						if point not in self.tribeset:
							self.tribeset[point] = 1
						else:
							self.tribeset[point] += 1
		return self.tribeset, self.conflicts

def load_tribemap(f, row):
	""" A helper function to load tribal-army maps
	from the text file
	"""
	maps = []
	for _ in range(row):
		maps.append(str(f.readline()).strip())

	return maps

def output_pretty(output_path, solutions):
	""" Parse solutions <dic:tribeset, int:n_conflicts>
	to an output file with desired answer format in Kalbrr
	"""
	f = open(output_path, "w")
	for idx, (tribes, n_conflicts) in enumerate(solutions):
		f.write("Case {}:\n".format(idx+1))
		for key, value in sorted(tribes.items()):
			f.write("{} {}\n".format(key, value))

		f.write("contested {}\n".format(n_conflicts))
	f.close()

def solve(input_path, output_path):
	f = open(input_path, "r")
	T = int(f.readline())
	solutions = []

	for _ in range(T):
		row = int(f.readline().strip())
		col = int(f.readline().strip())
		gmap = load_tribemap(f, row)

		g = G(row, col, gmap)
		tribeset, n_conflicts = g.countTribes()
		solutions.append((tribeset, n_conflicts))
	
	f.close()
	output_pretty(output_path, solutions)

def test_me():
	row, col = 12, 15
	gmap = [
		"############...",
		"#.......c.###..",
		"####......#.#..",
		".#.########.#..",
		"##...#..b#..#..",
		"#.a.#...#...###",
		"####.#.#d###..#",
		"......#...e#xx#",
		".#....#########",
		".#.x..#..#.....",
		".######.c#.....",
		"......####....."
	]

	row, col = 2, 2
	gmap = [
		".#",
		"#a"
	]

	# setup and initialise computation
	g = G(row, col, gmap)
	x = g.countTribes()

	print(x)


if __name__ == '__main__':
	solve("input.txt", "output.txt")