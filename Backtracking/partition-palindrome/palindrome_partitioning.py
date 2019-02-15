class Solution:

    def __init__(self):
        self.hashSet = {}

    def partition_palindrome(self, string):
        self.solution = {}
        self.hashSet = {}
        self.partition_palindrome_recursive([], string)
        return self.solution

    def partition_palindrome_recursive(self, partitioned, remaining):
        if (self.is_all_palindrome(partitioned)) and (self.is_all_palindrome([remaining])):
            result = partitioned[:] + [remaining] 
            self.solution[tuple(result)] = 1

        if not remaining:
            if (self.is_all_palindrome(partitioned)):
                self.solution[tuple(partitioned[:])] = 1
            return
        
        self.partition_palindrome_recursive(partitioned + [remaining[0]], remaining[1:])
        if partitioned:
            partitioned[-1] = partitioned[-1] + remaining[0]
            self.partition_palindrome_recursive(partitioned, remaining[1:])
    
    def is_all_palindrome(self, list_string):
        if not list_string:
            return False
        for string in list_string:
            if not string:
                return
            if string in self.hashSet:
                continue
            rev = string[::-1]
            if (rev == string) or len(string)==1:
                self.hashSet[string] = 1
                # print(string)
                continue
            else:
                return False
        return True

if __name__ == '__main__':
    solver = Solution()
    print(solver.partition_palindrome("efe").keys())