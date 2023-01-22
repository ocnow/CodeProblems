class Solution:
    def search(self, nums: list[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        start = nums[0]

        if target == start:
            return 0

        while j >= i:
            
            hlf = (i+j)//2
            print("i,j"+str((i,j)))
            print("hlf"+str(hlf))
            if target == nums[hlf]:
                return hlf
            

            if nums[hlf] >= start:
                #logic
                if target > nums[hlf]:
                    i = hlf + 1
                
                elif target < nums[hlf] and target > start:
                    j = hlf - 1
                
                elif target < nums[hlf] and target < start:
                    i = hlf + 1

            elif nums[hlf] < start:
                #logic
                if target < nums[hlf]:
                    j = hlf - 1
                
                elif target > nums[hlf] and target > start:
                    j = hlf - 1
                
                elif target > nums[hlf] and target < start:
                    i = hlf + 1

        return - 1

S1 = Solution()
print(S1.search([1],0))