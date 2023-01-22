class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dict = {}
        for i in range(len(nums)):
            if target - nums[i] in dict.keys():
                return [i, dict[target - nums[i]]]
            
            dict[nums[i]] = i