class Solution:
    def colorful(self, A):
        self.hashSet = {}
        self.prod = {}
        self.is_colorful = True

        if len(str(A)) == 1:
            return 1
        if self.is_duplicate(str(A)) or ('1' in str(A)):
            return 0

        self.colorful_recursive('', str(A))
        if self.is_colorful:
            return 1
        else:
            return 0
        
    def colorful_recursive(self, number_string, remaining_digits):
        if not self.is_colorful:
            return

        if (number_string != '') and not (number_string in self.hashSet):
            self.hashSet[number_string] = 1
            prod = self.digit_prod(number_string)
            # print(number_string, prod)
            if prod in self.prod:
                self.is_colorful = False
                return
            self.prod[prod] = 1

        if not remaining_digits:
            return

        self.colorful_recursive(number_string+remaining_digits[0], remaining_digits[1:])
        self.colorful_recursive(remaining_digits[0], remaining_digits[1:])
    
    def digit_prod(self, number_string):
        if not number_string:
            return 0
        result = 1
        for c in number_string:
            result *= int(c)
        return result
    
    def is_duplicate(self, number_string):
        myset = {}
        for x in number_string:
            if x in myset:
                return True
            myset[x] = 1
        return False

if __name__ == '__main__':
    solver = Solution()
    print(solver.colorful(1))