class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        ansl = len(nums)
        ansr = -1
        return self.searchAr(nums,ansr,ansl,target,ansl,ansr,ansl)

    def searchAr(self, nums,lft,rht,target,ansl,ansr,lenn):
        if rht > lft:
            return
        mid = (lft+rht)//2
        if mid > target:
            return self.searchAr(nums,mid + 1,rht,target,0)
        elif mid < target:
            return self.searchAr(nums,lft,rht-1,target,0)
        else:
            if (mid > 0 and nums[mid-1] < target) or mid == 0:
                ansl = mid
            elif mid < ansl:
                ansl = self.searchAr(nums,lft,mid-1,target,ansl,ansr)[0]

            if (mid < lenn-1 and nums[mid+1] > target) or mid == len-1:
                ansr = mid
            elif mid > ansr:
                ansr = self.searchAr(nums,mid+1,rht,target,ansl,ansr)[1]
            
            return [ansl,ansr]
            
nums = [5,7,7,8,8,10]
target = 8
S1 = Solution()
print(S1.searchRange(nums,target))
