class Solution:
    
    def isMatch(self, inpString: str, inpreg: str) -> bool:
        dp_results = {}
    
        def matchReg(i,j):
            
            
            if (i,j) in dp_results.keys():
                return dp_results[i,j]
            

            if j == len(inpreg):
                dp_results[i,j] = i == len(inpString)
                return dp_results[i,j]

                

            first_match =  i < len(inpString) and inpreg[j] in (inpString[i],'.')

            if j+1<len(inpreg) and inpreg[j+1] == '*':
                dp_results[i,j] =  (matchReg(i,j+2)) or (first_match and matchReg(i+1,j))
                
            else:
                dp_results[i,j] =  first_match and matchReg(i+1, j+1)

            return dp_results[i,j]

        return matchReg(0,0)