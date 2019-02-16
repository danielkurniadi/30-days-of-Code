class Solution:
    # @param A : integer
    # @return a list of integers
    def grayCode(self, n):
        self.solutions = [] 
        binaries = self.gray_code_recursive(n)

        for binary in binaries:
            self.solutions.append(int(binary,2))
        return self.solutions
            
    
    def gray_code_recursive(self, n, ):
        if n == 1:
            return ['0', '1']
        
        # mirror
        prev = self.gray_code_recursive(n-1)
        mirror_upper = prev
        mirror_bot = prev[::-1]

        # prefixing upper half mirror
        for i in range(len(mirror_upper)):
            mirror_upper[i] = '0' + mirror_upper[i]
        
        for i in range(len(mirror_bot)):
            mirror_bot[i] = '1' + mirror_bot[i]
        
        return mirror_upper + mirror_bot


if __name__ == '__main__':
    solver = Solution()
    result = solver.grayCode(4)
    print(result)