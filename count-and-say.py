class Solution:
    def countAndSay(self, n: int) -> str:
        prev = ("1",1)
        i = 1
        while i < n:
            prev = self.sayIt(prev)
            i = i + 1
        #print(prev[0])
        return prev[0]

        
    def sayIt(self,tple):
        ans = ""
        i = 0
        #l = len(nst)
        nlen = 0
        while i < tple[1]:
            chr = tple[0][i]
            tcnt = 1
            i = i + 1
            while i < tple[1] and tple[0][i] == chr:
                tcnt = tcnt + 1
                i = i + 1
            ans = ans + str(tcnt) + chr
            nlen += 2
        return ans,nlen

S1 = Solution()
print(S1.countAndSay(6))
        
