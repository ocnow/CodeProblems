from collections import deque

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:

        if digits == "":
            return []
        
        table = ["0", "1", "abc", "def", "ghi", "jkl",
             "mno", "pqrs", "tuv", "wxyz"]

        lis = []
        q = deque()
        q.append("")

        n = len(digits)

        while len(q) != 0:
            s = q.pop()

            if len(s) == n:
                lis.append(s)
            else:

                for letter in table[int(digits[len(s)])]:
                    q.append(s + letter)

        
        return lis


S1 = Solution()
print(S1.letterCombinations("23"))