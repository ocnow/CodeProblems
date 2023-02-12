class Solution:
    def simplifyPath(self, path: str) -> str:
        ar = path.split("/")
        ans = ""
        ar1 = []

        #print(ar)

        for a in ar:
            if a == "" or a == ".":
                continue
            
            if a == "..":
                if ar1:
                    ar1.pop()
                continue
            
            #print("appending")
            ar1.append(a)

        
        for a in ar1:
            ans+=a + "/"
        
        return "/" + ans[:-1]