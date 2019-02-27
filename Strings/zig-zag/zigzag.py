class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings
    def convert(self, s, n):
        length = len(s)
        self.indices = []
        if length<=n or n==1:
            return s
        for i in range(n):
            indices = [(i+(2*n-2)*j) for j in range(length//n+1) if (i+(2*n-2)*j)<length]
            indices2 = []
            if i!=0 or n>2:
                indices2 = [(-i+(2*n-2)*j) for j in range(length//n+1) if ((-i+(2*n-2)*j)<length  and (-i+(2*n-2)*j)>=0)]
            self.indices = self.indices + sorted(set(indices+indices2))

        return "".join([s[k] for k in self.indices])
        
if __name__ == '__main__':
    solver = Solution()
    x = solver.convert("BBB", 3)
    print(solver.indices)
    print(x)