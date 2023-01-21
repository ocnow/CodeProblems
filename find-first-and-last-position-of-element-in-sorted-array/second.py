class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        ar = [0,0]
        ar[0] = self.searchLeft(nums,target)
        ar[1] = self.searchRight(nums,target)
        return ar

    def searchLeft(self,nums,target):
        start = 0
        end = len(nums) - 1
        
        position = -1
        while end >= start:
            mid = (start + end)//2

            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                position = mid
                end = mid - 1
        return position
    
    def searchRight(self,nums,target):
        start = 0
        end = len(nums) - 1
        
        position = -1
        while end >= start:
            mid = (start + end)//2

            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                position = mid
                start = mid + 1
        return position
     
nums = [1,11,11]
target = 11
S1 = Solution()
print(S1.searchRange(nums,target))