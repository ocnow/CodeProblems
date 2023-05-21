from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def check(pos_indx_stack_ar,wi):
            ret = []
            for indx in pos_indx_stack_ar:
                if board[indx[-1][0]][indx[-1][1]] == word[wi]:
                    ret.append(indx)

            return ret

        def generate_combs(pos)
        

    #generate all starting indexes as stack
    #iterate over each and check adjucent which are not present in current stack
        #if match -> append to stack index
    #now repeat iterating over returning stack indexes

    #generate all 
        initial_stack = []
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                initial_stack.append([(i,j)])
        
        print(initial_stack)
        new_stack = check(initial_stack,0)
        print(new_stack)



S1 =Solution()
S1.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE")