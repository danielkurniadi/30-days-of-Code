class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    @classmethod
    def threeSum(self, Arr):
        if len(Arr)<=3:
            if sum(Arr)==0:
                return Arr
            return []
        solutions = set()
        Arr = sorted(Arr)
        for u in range(1, len(Arr)-1):
            target = Arr[u]
            i, j = u-1, u+1
            while(0<=i and j<len(Arr)):
                threesum = (Arr[i] + Arr[j] + target)
                if threesum == 0:
                    solutions.add((Arr[i], target, Arr[j]))
                    i -= 1
                    j += 1
                elif threesum < 0 :
                    j += 1
                else:
                    i -= 1

        print(sorted(solutions))
            
if __name__ == '__main__':
    A = [ 1, -4, 0, 0, 5, -5, 1, 0, -2, 4, -4, 1, -1, -4, 3, 4, -1, -1, -3 ]
    
    Solution.threeSum(A)