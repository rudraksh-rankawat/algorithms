class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        checkMapRow = [dict() for i in range(9)]
        checkMapCol = [dict() for i in range(9)]
        checkMapBox = [dict() for i in range(9)]
        def findBox(i, j):
            return (i // 3) * 3 + (j // 3) #logic to be thought

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                boxArrIndex = findBox(i, j)
                if val != ".": 

                    
                    checkMapRow[i][int(val)] = 1 + checkMapRow[i].get(int(val), 0)
                    checkMapCol[j][int(val)] = 1 + checkMapCol[j].get(int(val), 0)
                    checkMapBox[boxArrIndex][int(val)] = 1 + checkMapBox[boxArrIndex].get(int(val), 0)

                    if checkMapRow[i].get(int(val), 0) > 1:
                        return False
                    if checkMapCol[j].get(int(val), 0) > 1:
                        return False
                    if checkMapBox[boxArrIndex].get(int(val), 0) > 1:
                        return False
                    

        return True


            
        