class Solution:
    def canJump(self, nums: list[int]) -> bool:
        le = len(nums)
        current = 0
        farthest = 0
        #rng = nums[current]

        indx = 0
        while indx <= farthest:
            jmp = nums[indx] + indx
            if jmp >= le - 1:
                return True
            
            if jmp > farthest:
                farthest = jmp
            
            indx+=1
        
        return False