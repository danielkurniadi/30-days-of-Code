class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    @classmethod
    def threeSumClosest(cls, A, target):
        min_diff = 2**32
        closest = None
        A = sorted(A)

        # Check if array length condition doesn't support
        if len(A)<3:
            return None
        if len(A)==3:
            return sum(A)

        # iterate the array with each point to i - 1st element
        for i in range(len(A)-1):
            a = A[i]
            j, k = i+1, len(A)-1
            # iterate with 2nd & 3rd pointer j, k
            while j<k:
                three_sum = a + A[j] + A[k]
                # the ideal answer is if three sum equals target
                if three_sum == target:
                    return three_sum
                # not arriving at ideal answer, then evaluate if it is closer
                if abs(three_sum-target) < min_diff:
                    min_diff = abs(three_sum-target)
                    closest = three_sum
                # then decide next step
                if three_sum < target:
                    j += 1
                else:
                    k -= 1
        
        return closest

if __name__ == '__main__':
    A = [ 2, 1, -9, -7, -8, 2, -8, 2, 3, -8 ]
    target = -1
    closest = Solution.threeSumClosest(A, target)
    print(closest)