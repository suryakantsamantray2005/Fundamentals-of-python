class Solution:
    def sortColors(self,nums):
        freq={}
        largest=float('-inf')
        second_largest=float('-inf')
        third_largest=float('-inf')
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        for key in freq:
            if key > largest:
              third_largest = second_largest
              second_largest = largest
              largest = key

            elif key > second_largest:
              third_largest = second_largest
              second_largest = key

            elif key > third_largest:
              third_largest = key

        for j in 

obj=Solution()
print(obj.sortColors([2,0,2,1,1,0]))