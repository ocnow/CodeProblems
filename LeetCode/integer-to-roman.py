class Solution:
    def intToRoman1(self, num: int) -> str:
        if num == 0:
            return ""
        elif num >= 1000:
            return "M" + self.intToRoman(num-1000)
        elif num >= 900:
            return "CM" + self.intToRoman(num-900)
        elif num >= 500:
            return "D" + self.intToRoman(num-500)
        elif num >= 400:
            return "CD" + self.intToRoman(num-400)
        elif num >= 100:
            return "C" + self.intToRoman(num-100)
        elif num >= 90:
            return "XC" + self.intToRoman(num-90)
        elif num >= 50:
            return "L" + self.intToRoman(num-50)
        elif num >= 40:
            return "XL" + self.intToRoman(num-40)
        elif num >= 10:
            return "X" + self.intToRoman(num-10)
        elif num >= 9:
            return "IX" + self.intToRoman(num-9)
        elif num >= 5:
            return "V" + self.intToRoman(num-5)
        elif num >= 4:
            return "IV" + self.intToRoman(num-4)
        elif num >=1:
            return "I" + self.intToRoman(num-1)

    def intToRoman(self, num: int) -> str:
        stages = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        rletters = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
        romanStr = ""

        for i in range(12,-1,-1):
            romanStr = romanStr + (num//stages[i]) * rletters[i]

            num = num % stages[i]

            if num <= 0:
                break

        return romanStr


S1 = Solution()
print(S1.intToRoman(1994))
            