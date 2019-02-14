class Solution:
    # @return a list of list of integers
    def combinationSum(self, C, t):
        self.hashSet = {}
        self.TARGET = t
        self.combinationSum_recursive((), 0, sorted(C))
        return sorted(self.hashSet.keys())
        
    def combinationSum_recursive(self, chosen, sum, remaining):
        if sum == self.TARGET:
            self.hashSet[chosen] = 1
        if (not remaining) or sum >=self.TARGET:
            return
        self.combinationSum_recursive(chosen, sum, remaining[1:])
        self.combinationSum_recursive(chosen+(remaining[0],), sum+remaining[0], remaining[1:])
