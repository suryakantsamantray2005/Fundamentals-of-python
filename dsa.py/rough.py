class Solution:
    def maximumProduct(self,nums):
        first=float('-inf')
        second=float('-inf')
        third=float('-inf')
        second_min=float('inf')
        minimum=float('inf')
        for i in nums:
            if i!=first or i!=second or i!=third:
              if i>first:
                first=i
              elif i<=first and second<i:
                second=i
              elif i<=first and i<=second and i>third:
                 third=i

        for j in nums:
           if j!=second_min or j!=minimum:
              if j<minimum:
                 minimum=j
                 if j>=minimum and j<second_min:
                    second_min=j

        return max(first*second*third,minimum*second_min*first)
obj=Solution()
print(obj.maximumProduct([1,2,3,4]))