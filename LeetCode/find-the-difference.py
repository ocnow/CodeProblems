class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ar = [0 for i in range(26)]

        for si in s:
            ar[ord(si) - 97]+=1
        
        for si in t:
            p = ord(si) - 97
            if ar[p] == 0:
                return si
            ar[p]-=1