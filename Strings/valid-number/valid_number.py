class Solution:
    # @param A : string
    # @return an integer
    def isNumber(self, num):
        import re
        x = re.search(r'^\s*?\-?(([0-9]+\.[0-9]+)|(\.?[0-9]+))(e?\-?[0-9]+)?\s*$', num)
        if x:
            return 1
        return 0
        
if __name__ == '__main__':
    import re
    solver = Solution()
    good_num = ["-901.99", " 0.1 ", " 2e10 ", "-01.1e-90  ", ".199", ".190e190", "-0.133e90    ", "1297356"] #6
    print("goodnum")
    for num in good_num:
        print(solver.isNumber(num))
    bad_num = ["0.", "3.", "2e9.8"]
    print("badnum")
    for num in bad_num:
        print(solver.isNumber(num))

    