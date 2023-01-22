class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        res = len(strs[0])
        for i in range(len(strs) - 1):
            #print(res)
            m = min(res,len(strs[i+1]))
            t = 0
            for j in range(m):
                if(strs[i][j] != strs[i+1][j]):
                    break
                t = t + 1
            
            res = t


        #print(res)
        return strs[0][:res]

S1 = Solution()
S1.longestCommonPrefix(["flower","flow","flight"])
            

                
                



