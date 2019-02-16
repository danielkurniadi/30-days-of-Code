class Solution:
    def __init__(self):
        self.hashSet = {}

    def getPermutation(self, n, k):
        if k > self.factorial(n):
            return [], ()
        self.K = k
        self.RANK = 1
        self.solution = []
        self.hashSet = {} #for factorial
        Arr = [i for i in range(1, n+1)]

        self.get_kth_recursive([], Arr, 1)
        return self.solution

    def get_kth_recursive(self, chosen, remaining, count):
        if not remaining:
            self.solution.append((chosen[:], count))
            self.RANK +=1
            return
        # explore combination
        depth = len(remaining)
        m = self.factorial(depth-1)
        for i,e in enumerate(remaining):
            m1, m2 = count+m*i, count+m*(i+1)
            if m1<=self.K and self.K<=m2:
                chosen.append(e)
                remaining.pop(i)
                self.get_kth_recursive(chosen, remaining, m1)
                remaining.insert(i, chosen.pop())

    def factorial(self, n):
        result = 1
        if n==0:
            return 0
        if n == 1 :
            return 1
        if n in self.hashSet:
            return self.hashSet[n]
        for i in range(1, n+1):
            result = result * i
        self.hashSet[n] = result
        return result

if __name__ == '__main__':
    solver = Solution()
    # print(solver.factorial(4))
    solver.getPermutation(4, 23)
    print(solver.solution)