class Solution:
    # @param A : string
    # @return a list of strings
    def letterCombinations(self, A):
        Arr = [int(x) for x in A]
        self.telephone_btn_map = {
            0:'0', 1:'1', 2: "abc", 3: "def",
            4: "ghi", 5: "jkl", 6: "mno",
            7: "pqrs", 8: "tuv", 9 :"wxyz"
        }
        self.SIZE = len(Arr)
        self.board = [self.telephone_btn_map[number] for number in Arr]
        self.current = ""
        self.solution = []

        self.lettercomb_recursive(0)

    def lettercomb_recursive(self, col):
        if col == self.SIZE:
            self.solution.append((self.current+'.')[:-1])
            return
        letters = self.board[col]
        for letter in letters:
            self.current += letter
            self.lettercomb_recursive(col+1)
            self.current = self.current[:-1]

if __name__ == '__main__':
    solver = Solution()
    solver.letterCombinations("0130482571")
    print(solver.solution)