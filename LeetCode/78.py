class Solution:
    def subsets_binary(self, nums: List[int]) -> List[List[int]]:
        output = []
        ln = len(nums)
        total_subsets = 2 ** ln
        nth_bit = 1 << ln
        for i in range(total_subsets):
            bitmask = bin(i | nth_bit)[3:]
            output.append([nums[x] for x in range(ln) if bitmask[x] == '1'])
            
        return output

    def subsets(self,nums : List[int]) -> List[List[int]]:
        def backtrack(size_needed,starting_index,ln,curr):
            if len(curr) == size_needed:
                output.append(curr[:])
                return
            
            for i in range(starting_index,ln):
                curr.append(nums[i])
                
                #output.append(curr)

                backtrack(size_needed,i+1,ln,curr)

                curr.pop()
            
        
        output = []
        ln = len(nums)
        for size_needed in range(ln+1):
            backtrack(size_needed,0,ln,[])
        return output
