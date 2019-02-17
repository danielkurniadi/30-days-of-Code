class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, Mat, n):
        Arr = []
        if not Mat:
            return 0
        for arr in Mat:
            if not arr:
                continue
            if (arr[0] <= n) and (n <= arr[-1]):
                Arr = arr
                print(Arr)
                break
        if not Arr:
            return 0

        i, j = 0, len(Arr)-1
        while i <= j:
            mid = (i+j)//2
            if Arr[mid] == n:
                print(Arr[mid])
                return 1
            elif Arr[mid] < n:
                i = mid + 1
            else:
                j = mid -1
        return 0

if __name__ == '__main__':
    solver = Solution()
    Mat = [
        [1,   3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    is_found = solver.searchMatrix(Mat, 11)
    print(is_found)


