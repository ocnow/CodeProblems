class Solution:
    def threeSum(self,nums: list[int], target:int) -> list[list[int]]:
        ret = []
        sz = len(nums)

        for i in range(sz - 1):
            if(i > 0 and nums[i] == nums[i-1]):
                continue

            if(nums[i] > target and target > 0):
                break

            if(target < 0 and nums[sz-1] < 0 and nums[i] < target):
                break

            low = i + 1
            high = sz - 1

            while low < high:
                if low > i + 1 and nums[low] == nums[low - 1]:
                    low = low + 1
                    continue

                if high < sz - 1 and nums[high] == nums[high + 1]:
                    high = high - 1
                    continue

                tsum = nums[i] + nums[low] + nums[high]

                if tsum == target:
                    ret.append([nums[i],nums[low],nums[high]])
                    low = low + 1
                    high = high - 1

                elif tsum > target:
                    high = high - 1

                elif tsum < target:
                    low = low + 1
        
        return ret

    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        ret = []
        sz = len(nums)
        for i in range(sz-1):

            if(i > 0 and nums[i] == nums[i-1]):
                continue

            if(nums[i] >  target and target > 0):
                break

            if(target < 0 and nums[sz-1] < 0 and nums[i] < target):
                break

            ans = self.threeSum(nums[i+1:],target - nums[i])

            if(len(ans) != 0):
                for ar in ans:
                    ret.append([nums[i]] + ar)
        
        return ret

S1 = Solution()

ar = [1,-2,-5,-4,-3,3,3,5]
trgt = -11

print(S1.fourSum(ar,trgt))
#print(S1.threeSum([-1,1,1,2,2],1))
