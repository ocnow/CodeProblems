class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        arr,i = self.reverseArray(nums,len(nums)-1)
        return arr

    def reverseArray(self,nums,lastIndex):
        i = lastIndex
        while i > 0 and nums[i-1] > nums[i]:
            i = i - 1

        print("current i"+str(i))
        l = (lastIndex - i)+1
        print(l)
        for j in range(i,l // 2):
            nums[j], nums[l - j - 1] = nums[l - j - 1], nums[j]
        
        return (nums,i)

    def reverseArray1(self,nums,lastIndex):
        i = lastIndex - 1
        print(i)
        nums = nums[-1 * i:]
        return (nums,i)
    
        


ar1 = [3,8,7,6,2]
S1 = Solution()
print(S1.reverseArray1(ar1,len(ar1)-1))