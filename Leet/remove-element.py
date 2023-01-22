class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        cor_indx = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[cor_indx] = nums[i]
                cor_indx+=1
        
        return cor_indx
