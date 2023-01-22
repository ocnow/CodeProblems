class Solution:
    #solution by me
    def maxArea1(self, height: list[int]) -> int:
        i = 0
        tempArea = 0
        arLength = len(height)
        for i in range(arLength):
            for j in range(i+1,arLength):
                if height[i] > height[j]:
                    area = height[j] * (j-i)
                else:
                    area = height[i] * (j-i)
                if area > tempArea:
                    tempArea = area
                print("area:"+str(area))
                print("temparea:"+str(tempArea))
        
        return tempArea

    #viewed solution
    def maxArea(self,height: list[int]) -> int:
        left = 0
        right = len(height)-1
        area = 0
        while right > left:
            tarea = min(height[left], height[right]) * (right - left)

            if tarea > area:
                area = tarea
            
            if height[left] < height[right]:
                left = left + 1
            elif height[left] > height[right]:
                right = right - 1
            else:
                left = left + 1
                right = right - 1
        return area

S1 = Solution()
height = [1,8,6,2,5,4,8,3,7]
print(S1.maxArea(height))



