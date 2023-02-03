class Solution:
    def hammingWeight(self, n: int) -> int:
        k = "{0:b}".format(n)
        return k.count('1')