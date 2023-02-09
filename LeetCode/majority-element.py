class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        sz = len(nums)
        if sz == 1:
            return nums[0]
        for num in nums:
            if num in dict.keys():
                dict[num] += 1
                if dict[num] > sz//2:
                    return num
                continue
            
            dict[num] = 1