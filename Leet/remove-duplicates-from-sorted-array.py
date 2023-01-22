class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0
        orig_indx = 0
        for i in range(1,len(nums)):
            if nums[i] != nums[orig_indx]:
                nums[orig_indx+1] = nums[i]
                orig_indx+=1
            
        return orig_indx+1
