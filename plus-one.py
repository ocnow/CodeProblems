class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1,-1,-1):
            digits[i] = digits[i] + carry
            if digits[i] == 10:
                carry = 1
                digits[i] = 0
                continue
            carry = 0

        if carry == 1:
            return [1] + digits  
        return digits
