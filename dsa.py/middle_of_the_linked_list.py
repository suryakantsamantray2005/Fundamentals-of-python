# finding the middle element in the linked list
# # Brute force approach 
class Solution:
    def middleNode(self, head):
        n=0
        temp=head
        while temp is not None:
            n+=1
            temp=temp.next
        temp=head
        for i in range(0,n//2):
            temp=temp.next
        return temp
# time complexity - O(n+n/2) and space complexity - O(1)