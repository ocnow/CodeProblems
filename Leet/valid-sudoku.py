class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        while True:
            #rowCheck
            i = 0
            while i < 9:
                j = 0
                dicrow = [0 for i in range(9)]
                diccol = [0 for i in range(9)]
                dicbox = [0 for i in range(9)]
                while j< 9:
                    print("(i,j)"+str((i,j))+"================================")
                    if board[i][j] == '.':
                        board[i][j] = 0
                    
                    if board[j][i] == '.':
                        board[j][i] = 0

                    if board[(i//3 * 3) + j//3][(i%3 * 3)+(j%3)] == '.':
                        board[(i//3 * 3) + j//3][(i%3 * 3)+(j%3)] = 0
                    
                    rnm = int(board[i][j]) - 1
                    cnm = int(board[j][i]) - 1
                    bnm = int(board[(i//3 * 3) + j//3][(i%3 * 3)+(j%3)]) - 1

                    print("rnm"+str(rnm))
                    print("cnm"+str(cnm))
                    print("bnm"+str(bnm))

                    if rnm != -1:
                        if dicrow[rnm] == 0:
                            dicrow[rnm] = 1
                        else:
                            print("failedr->"+str((i,j)))
                            print("failedr->"+str(dicrow))
                            return False

                    if cnm != -1:
                        if diccol[cnm] == 0:
                            diccol[cnm] = 1
                        else:
                            print("failedc->"+str((i,j)))
                            print("failedr->"+str(diccol))
                            return False

                    if bnm != -1:
                        print("bnm:=>"+str(bnm))
                        if dicbox[bnm] == 0:
                            dicbox[bnm] = 1
                        else:
                            print("failedb->"+str((i,j)))
                            print("failedr->"+str(dicbox))
                            return False

                    j+=1
                i+=1
            print("returning true-------------")
            return True

pzle = [["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]]

S1 = Solution()
S1.isValidSudoku(pzle)

