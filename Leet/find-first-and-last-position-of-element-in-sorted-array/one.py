class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        ansl = len(nums)
        ansr = -1
        return self.searchAr(nums,0,ansl-1,target,ansl,ansr,ansl)

    def searchAr(self, nums,lft,rht,target,ansl,ansr,lenn):
        
        print([lft,rht,target,ansl,ansr,lenn])
        if rht < lft:
            return [-1,-1]
        mid = (lft+rht)//2
        print("mid"+ str(mid))
        if nums[mid] > target:
            print("lftchk")
            return self.searchAr(nums,lft,mid-1,target,ansl,ansr,lenn)
        elif nums[mid] < target:
            print("rghtchk")
            return self.searchAr(nums,mid+1,rht,target,ansl,ansr,lenn)
        else:
            print("eqchk")
            if (mid > 0 and nums[mid-1] < target) or mid == 0:
                ansl = mid
            elif mid < ansl:
                ansl = self.searchAr(nums,lft,mid-1,target,ansl,ansr,lenn)[0]

            if (mid < lenn-1 and nums[mid+1] > target) or mid == lenn-1:
                ansr = mid
            elif mid > ansr:
                ansr = self.searchAr(nums,mid+1,rht,target,ansl,ansr,lenn)[1]
            
        return [ansl,ansr]
     
nums = [11,11]
target = 11
S1 = Solution()
print(S1.searchRange(nums,target))