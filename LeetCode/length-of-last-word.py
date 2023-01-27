class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.rstrip().split(" ")[-1])

S1 = Solution()
print(S1.lengthOfLastWord("   fly me   to   the moon  "))
