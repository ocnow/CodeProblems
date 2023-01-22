class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        st = 0
        en = len(nums) - 1
        le = len(nums)
        
        while en >= st :
            print("st:"+str(st))
            print("en:"+str(en))
            i = (st + en)//2
            if nums[i] == target:
                return i
            if nums[i] < target:
                if i + 1 >= le or nums[i+1] > target:
                    return i + 1
                st = i + 1
            elif nums[i] > target:
                if i - 1 < 0 or nums[i-1] < target:
                    return i
                en = i - 1
            
S1 = Solution()
ar = [1,3,5,6,7,8,9]
target = 0

print(S1.searchInsert(ar,target))
