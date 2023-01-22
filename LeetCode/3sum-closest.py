0/5
class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        
        nums.sort()
        res = 0
        lenn = len(nums)
        prev_diff = 10000001
        #ans = 0

        #print(nums)
        for i in range(lenn):

            if i>0 and nums[i] == nums[i-1]:
                continue

            # if i>0 and prev_diff < 0:
            #     break

            low = i + 1
            high = lenn - 1

            while high > low:
                summ = nums[i] + nums[low] + nums[high]
                diff = target - summ

                if diff == 0:
                    return target

                elif abs(diff) < abs(prev_diff):
                    prev_diff = diff
                    res = summ

                if summ > target:
                    high = high - 1
                
                else:
                    low = low + 1
            
        return res
   

S1 = Solution()
print(S1.threeSumClosest([-1,2,1,-4],1))
                    

#first negative is the answer?
#if first negative is worse than previous positive then stop that shit

#for positive, is there any shortcut?

            
