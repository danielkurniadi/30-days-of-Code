class Solution:
	# @param A : list of integers
	# @return a list of list of integers
	def subsetsWithDup(self, Arr):
		self.hashSet = {}
		self.subsets_recursive((), sorted(Arr))
		return sorted(self.hashSet.keys())

	def subsets_recursive(self, chosen, remaining):
		if not remaining:
			self.hashSet[chosen] = 1
			return
		self.subsets_recursive(chosen, remaining[1:])
		self.subsets_recursive(chosen+(remaining[0],), remaining[1:])

if __name__ == '__main__':
	solver = Solution()
	result = solver.subsetsWithDup([1, 2, 2])
	print(result)