class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        s = s.lower()
        while j > i:
            if not self.isalnum(s[i]):
                i = i + 1
                continue
            if not self.isalnum(s[j]):
                j = j - 1
                continue
            
            if s[i] != s[j]:
                return False

            i = i + 1
            j = j - 1
            
        return True

    def isalnum(self,chr):
        vs = ['0','1','2','3','4','5','6','7','8','9','a', 'b', 'c', 'd', 'e', 'f','g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        if chr in vs:
            return True