class BaseSolution:
    @classmethod
    def merge(cls, A, B):
        pass

class Solution(BaseSolution):
    # @param A : list of integers
    # @param B : list of integers
    @classmethod
    def merge(cls, A, B):
        # A = sorted(A)
        # B = sorted(B)
        n = len(A)
        m = len(B)
        
        # If one or both of the array is empty
        if n == 0:
            return B
        if m == 0:
            return A
        
        # initialize index pointers
        i, j = 0, 0
        C = []
        while (i<n) and (j<m):
            a, b = A[i], B[j]
            if a <= b :
                C.append(a)
                i += 1
            else:
                C.append(b)
                j += 1
        
        while (i<n):
            C.append(A[i])
            i += 1
        
        while (j<m):
            C.append(B[j])
            j += 1
        
        return C


if __name__ == '__main__':
    A = [-4, 3]
    B = [-2, -2]
    C = Solution.merge(A, B)
    print(C)