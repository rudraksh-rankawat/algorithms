class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        checkMapRow = [dict() for i in range(9)]
        checkMapCol = [dict() for i in range(9)]
        checkMapBox = [dict() for i in range(9)]
        def findBox(i, j):
            if 0 <= i <= 2:
                if 0 <= j <= 2:
                    return 0
                if 3 <= j <= 5:
                    return 1
                if 6 <= j <= 8:
                    return 2

            if 3 <= i <= 5:
                if 0 <= j <= 2:
                    return 3
                if 3 <= j <= 5:
                    return 4
                if 6 <= j <= 8:
                    return 5
            
                
            if 6 <= i <= 8:
                if 0 <= j <= 2:
                    return 6
                if 3 <= j <= 5:
                    return 7
                if 6 <= j <= 8:
                    return 8

        for i in range(9):
            for j in range(9):
                valR = board[i][j]
                valC = board[j][i]
                if valR != ".": 
                    checkMapRow[i][int(valR)] = 1 + checkMapRow[i].get(int(valR), 0)
                if valC != ".": 
                    checkMapCol[i][int(valC)] = 1 + checkMapCol[i].get(int(valC), 0)
                
                boxArrIndex = findBox(i, j)
                if board[i][j] != ".":
                    checkMapBox[boxArrIndex][int(board[i][j])] = 1 + checkMapBox[boxArrIndex].get(int(board[i][j]), 0)

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val != ".":

                    if checkMapRow[i].get(int(val), 0) > 1:
                        return False
                    if checkMapCol[j].get(int(val), 0) > 1:
                        return False
                    if checkMapBox[findBox(i,j)].get(int(val), 0) > 1:
                        return False

        return True


            
        