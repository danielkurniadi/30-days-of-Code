class Solution:
    # @param n : integer
    # @return a list of strings
    def generateParenthesis(self, n):
        self.SIZE = n
        self.solutions = []
        
        if n < 1:
            return []

        self.generate_parenthesis_recursive("(", 1, 0)
        return sorted(self.solutions)
    
    def generate_parenthesis_recursive(self, parenthesis,countleft, countright):
        if countleft == self.SIZE:
            if countright < countleft:
                parenthesis = parenthesis + ')' * (countleft-countright)
            self.solutions.append(parenthesis)
            return
        
        parenthesis1 = parenthesis + '('
        self.generate_parenthesis_recursive(parenthesis1, countleft+1, countright)

        if countright < countleft:
            parenthesis2 = parenthesis + ')'
            self.generate_parenthesis_recursive(parenthesis2, countleft, countright+1)
        
if __name__ == '__main__':
    solver = Solution()
    solver.generateParenthesis(4)
    print(solver.solutions)
