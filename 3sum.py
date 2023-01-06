class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []

        lenn = len(nums)
        
        for i in range(0,lenn):

            if i> 0 and nums[i] == nums[i-1]:
                continue

            if nums[i] > 0:
                break 

            low = i+1
            high = lenn - 1

            #print("==================")
            while high > low:

                #handle case when low and high numbers are same    
                if low > i+1 and nums[low] == nums[low - 1]:
                    low = low + 1
                    continue

                if high < lenn - 1 and nums[high] == nums[high + 1]:
                    high = high - 1
                    continue

                tsum = nums[i] + nums[low] + nums[high]

                if tsum == 0:
                    res.append([nums[i],nums[low],nums[high]])
                    low = low + 1
                    high = high - 1
                
                elif tsum > 0:
                    high = high - 1
                
                elif tsum < 0:
                    low = low + 1

                #print("test")

        return res

S1 =Solution()
print(S1.threeSum([-1,0,1,2,-1,-4]))








