# container with most water leetcode 11
class Solution:
    def maxArea(self,height):
        max_water=0
        i=0
        j=len(height)-1
        while i<j:
            if height[i]>height[j]:
                area=min(height[i],height[j])*(j-i)
                j-=1
                if area>max_water:
                    max_water=area
            else:
                area=min(height[i],height[j])*(j-i)
                i+=1
                if area>max_water:
                    max_water=area
        return max_water
            
# time complexity - O(n) and space complexity - O(1)
obj=Solution()
print(obj.maxArea([1,8,6,2,5,4,8,3,7]))