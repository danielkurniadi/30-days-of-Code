class Solution:
    # @param A : integer
    # @return a list of list of strings
    def solveNQueens(self, A):
        self.SIZE = A
        self.all_boards_solution = []
        self.board = []
        self.queen_recursive(0)
        return self.all_boards_solution

    def queen_recursive(self, col):
        if col == self.SIZE:
            board = list(self.board)
            self.all_boards_solution.append(board)
            return
        # iterate all the possible rows
        for row in range(self.SIZE):
            # check whether the position is valid
            valid = True
            for (col2, row2) in self.board:
                if (col2 == col) or (row2 == row):
                    valid = False
                    break
                m = (row2-row)/(col2-col)
                if (m==1) or (m==-1):
                    valid = False
                    break
            if valid:
                # if valid, place the queen
                self.board.append((col, row))
                self.queen_recursive(col+1)
                self.board.pop()

if __name__ == '__main__':
    solver = Solution()
    boards = solver.solveNQueens(1)
    print(len(boards), "finish")