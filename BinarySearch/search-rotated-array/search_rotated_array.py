class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchRotated(self, Arr, target):
        left, right = 0, len(Arr)-1
        while left <= right:
            mid = (left+right)//2
            if Arr[mid] == target:
                return mid
            if Arr[left] == target:
                return left
            if Arr[right] == target:
                return right

            if Arr[mid] >= Arr[left]:
                # in the leftside
                if Arr[left] <= target <= Arr[mid]:
                    # if target fall in the range of left-mid, go left
                    right = mid -1
                else:
                    # go right
                    left = mid + 1
            else:
                # in the rightside
                if Arr[mid] <= target <= Arr[right]:
                    # if target fall in the range of mid-right, go right
                    left = mid + 1
                else:
                    right = mid -1

        return "Key not found"

if __name__ == '__main__':
    solver = Solution()
    Arr = [30, 40, 50, 10, 20]
    for x in Arr:
        result = solver.searchRotated(Arr, x)
        print("position/index: ", result)   

    for x in range(11, 31, 10):
        result = solver.searchRotated(Arr, x)
        print("position/index: ", result)

    for x in range(1, 30):
        result = solver.searchRotated(Arr, x)
        print("position/index: ", result)   


                



       
