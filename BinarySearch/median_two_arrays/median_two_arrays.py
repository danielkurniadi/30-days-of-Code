class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double
    def findMedianSortedArrays(self, A, B):
        if len(A)>len(B):
            A, B = B, A
        
        m, n = len(A), len(B)
        i, j = 0, n

        if not A:
            if (n)%2 == 0:
                    return float(B[n//2]+B[n//2-1])/2
            else:
                return B[n//2]
        if not B:
            if m%2 == 0:
                return float(A[m//2]+A[m//2-1])/2
            else:
                return A[n//2]
        
        if A[-1] < B[0]:
            # median is in B
            if m==n:
                return (A[-1]+B[-1])/2
            if (m+n)%2 == 0:
                    return float(B[n//2]+B[n//2-1])/2
            else:
                p = (m+n)//2 - m
                return B[p]

        while i <= j:
            print("======================")
            midB = (i+j)//2
            midA = (n+m)//2 - midB - 1
            if midB+1 > n-1 or midA < 0:
                j = midB -1
                continue
            if midB < 0 or midA > m-1:
                i = midB + 1

if __name__ == '__main__':
    solver = Solution()
    x = solver.findMedianSortedArrays([-5, 3, 6, 12, 15], [-12, -10, -6, -3, 4, 10])
    print(x)    

            
            




