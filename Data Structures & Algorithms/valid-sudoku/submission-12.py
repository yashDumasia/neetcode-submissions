class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        x = []
        y = []

        for i in range(9):
            for j in range(9):
                
                if board[i][j] != ".":

                    if board[i][j] not in x:
                        x.append(board[i][j])
                    else :
                        return False

                if board[j][i] != ".":
                    
                    if board[j][i] not in  y:
                        y.append(board[j][i])
                    else : 
                        return False

            x.clear()
            y.clear()

        for row in range(0, 9, 3):
            for col in range(0, 9, 3):

                box = []

                for i in range(row, row + 3):
                    for j in range(col, col + 3):

                        if board[i][j] == ".":
                            continue

                        if board[i][j] not in box:
                            box.append(board[i][j])
                        else:
                            return False

        return True