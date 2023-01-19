class Solution:
    def search(self, nums: list[int], target: int) -> int:
        #check if greater than start -
        #if it is - considering ascending array then quicksort
        #it it is less - considering descending then quick

        first_ele = nums[0]
        #check for perfect ascending 
        if target > first_ele:
            i = 0
            j = len(nums) - 1

            while j >= i:
                print("i,j"+str((i,j)))
                hlf = (i+j)//2
                print("half:" + str(hlf))
                if nums[hlf] == target:
                    return hlf

                elif target < nums[hlf]:
                    j = hlf - 1

                elif nums[hlf] > first_ele and target > nums[hlf]:
                    i = hlf + 1

                elif nums[hlf] < first_ele:
                    j = hlf - 1

        elif target < first_ele:
            i = 0 
            j = len(nums) - 1
            while j >= i:
                print("i,j"+str((i,j)))
                hlf = (i+j)//2
                print("half:" + str(hlf))
                if nums[hlf] == target:
                    return hlf
                
                
                elif nums[hlf] > first_ele:
                    i = hlf + 1
                
                elif nums[hlf] < first_ele and target < nums[hlf]:
                    j = hlf - 1
                
                elif nums[hlf] < first_ele and target > nums[hlf]:
                    i = hlf + 1

        
        elif target == first_ele:
            return 0

        return -1

S1 = Solution()
print(S1.search([4,5],7))