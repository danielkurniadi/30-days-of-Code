class BaseSolution():
    @classmethod
    def intersect(cls, A, B):
        pass

class Solution(BaseSolution):
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    @classmethod
    def intersect(cls, A, B):
        # A = sorted(A)
        # B = sorted(B)
        n = len(A)
        m = len(B)

        # If one of the array is empty
        # hence no intersection
        if n == 0:
            return []
        if m == 0:
            return []

        # Iterate with 2 pointers
        i, j = 0, 0
        intersects = []
        while (i<n) and (j<m):
            # Check found common element
            if A[i] == B[j]:
                intersects.append(A[i]) # push into list of commons
                i += 1
                j += 1
            elif A[i]< B[j]:
                i += 1
            else:
                j += 1
        
        return intersects


if __name__ == '__main__':
    A = [ 4, 5, 5, 5, 8, 9, 10, 10, 10, 11, 11, 12, 13, 14, 14, 15, 18, 20, 21, 21, 22, 22, 26, 26, 28, 29, 30, 30, 35, 35, 36, 37, 38, 38, 41, 41, 45, 45, 47, 47, 49, 50, 50, 50, 50, 53, 
        62, 66, 67, 70, 72, 74, 75, 75, 77, 79, 79, 81, 85, 91, 92, 92, 96, 99, 99 ]
    B = [ 1, 4, 4, 8, 10, 13, 18, 19, 21, 21, 24, 24, 24, 24, 24, 25, 26, 28, 28, 29, 30, 31, 32, 33, 36, 38, 39, 51, 52, 53, 56, 56, 57, 58, 59, 60, 61, 62, 64, 67, 67, 70, 70, 72, 72, 74, 77, 77, 78, 
        79, 80, 83, 85, 86, 86, 93, 93, 96, 97, 97, 97, 98, 98, 99, 101 ]
    C = Solution.intersect(A, B)
    print(C)
