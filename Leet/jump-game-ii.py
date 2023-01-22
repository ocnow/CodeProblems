class Solution:
    def jump1(self, nums: list[int]) -> int:
        le = len(nums)
        nums[le-1] = 0
        #dp = [0 for i in range(le)]

        for i in range(le-2,-1,-1):
            t = nums[i]
            k = 1
            jmp = 10001
            while k <= t:
                if i+k < le and nums[i+k] < jmp:
                    jmp = nums[i+k]
                k+=1
            nums[i] = jmp + 1
            #print(dp)
        
        return nums[0]

    def jump(self,nums: list[int]) -> int:
        le = len(nums)
        current = 0
        farthest = -1
        jumps = 0

        for i in range(le-1):
            if nums[i] + i > farthest:
                farthest = nums[i] + i
            
            if i == current:
                current = farthest
                jumps += 1
        
        return jumps