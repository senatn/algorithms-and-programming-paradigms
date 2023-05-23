class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        counter = 0

        for i in range(9):
            x_line = [0] * 9
            y_line = [0] * 9
            sub_box = [0] * 9
            for x in board[i]:
                x_line[x - 1] += 1
            for x in x_line:
                if x > 1:
                    counter +=1
            for y in board[y][i]:
                y_line[y - 1] +=1
            for y in y_line:
                if y > 1:
                    counter +=1
            