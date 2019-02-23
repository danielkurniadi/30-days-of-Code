class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        
        n, result = len(A), 0
        for i in range(n):
            if A[i] in ['a', 'e', 'i', 'o', 'u', 'A', 'I', 'U', 'E', 'O']:
                result += (n-i)
        return result