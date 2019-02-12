class ImprovedSolution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsets(self, Arr):
        self.SIZE = len(Arr)
        return sorted(self.subset_recursive([], sorted(Arr)))
    
    def subset_recursive(self, chosen, remaining):
        if len(remaining) == 0:
            return [chosen]        
        return self.subset_recursive(chosen, remaining[1:]) + self.subset_recursive(chosen+[remaining[0]], remaining[1:])

class BruteSolution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsets(self, Arr):
        self.hashSet = {}
        self.subset_recursive(Arr)
        temp = [x for x in self.hashSet.keys()]
        result = sorted(temp)
        result.insert(0, [])
        return result
        
    def subset_recursive(self, remaining):
        if len(remaining) == 0:
            return

        for i,x in enumerate(remaining):
            if not (tuple(remaining) in self.hashSet):
                self.hashSet[tuple(remaining)] = 1
            remaining.pop(i)
            if not ((x,) in self.hashSet):
                self.hashSet[(x,)] = 1
            self.subset_recursive(remaining)
            remaining.insert(i, x)            


if __name__ == '__main__':
    solver = BruteSolution()
    result = solver.subsets([ 8, 5, 19, 11, 10, 7, 18, 16, 13, 17 ])
    print((result))

