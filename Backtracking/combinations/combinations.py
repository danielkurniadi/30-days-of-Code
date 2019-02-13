class Solution:
    """
    Given two integers n and k, return all possible combinations of k numbers out of 1 2 3 ... n.
    Make sure the combinations are sorted.

    To elaborate,
    Within every entry, elements should be sorted. [1, 4] is a valid entry while [4, 1] is not.
    Entries should be sorted within themselves.

    If n = 4 and k = 2, a solution is:
    [1,2], [1,3],[1,4],[2,3],[2,4],[3,4]
    """

    def combine(self, n, k):
        """Generate unique combinations of k numbers from n consecutive numbers
        """
        # Initialize hashset to track unique combination using dictionary
        self.SIZE = k
        self.hashSet = {}
        # Begin recursive combinations
        remaining = [i for i in range(1, n+1)]
        self.combine_recursive((), tuple(remaining))
        # Clean and return result
        return sorted(self.hashSet.keys())

    def combine_recursive(self, chosen, remaining):
        if len(chosen) == self.SIZE:
            self.hashSet[chosen] = 1
            return
        if not remaining:
            return
        self.combine_recursive(chosen, remaining[1:])
        self.combine_recursive(chosen+(remaining[0],), remaining[1:])

if __name__ == '__main__':
    solver = Solution()
    solver.combine(8, 4)
    result = sorted(solver.hashSet.keys())
    print(result)
    