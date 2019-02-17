class Solution:
    def solve(self ,n):
        s = 1
        e = n
        hashSet = {0:0, 1:1, 2:1, 3:1, 4:2, 5:2, 6:2, 7:2, 8:2, 9:3, 16:4, 25:5, 36:6, 49:7, 64:8, 81:9}
        if n in hashSet:
            return hashSet[n]
        while s <= e:
            mid = (s+e)//2
            if (int(mid)*int(mid)==n):
                return int(mid)
            if (n-1 <= mid*mid) and (mid*mid <=(n)):
                if int(mid)*int(mid) > n:
                    mid = mid-1
                return int(mid)
            elif mid*mid < n:
                s = mid+1
            else:
                e = mid-1

        if int(mid)*int(mid) > n:
            mid = int(mid)-1
        return mid

if __name__ == '__main__':
    solver = Solution()
    x = solver.solve(930675566)
    print(x)