# reversing a linked list
class Solution:
    def reverseList(self, head):
        prev=None
        temp=head
        while temp is not None:
            front=temp.next
            temp.next=prev
            prev=temp
            temp=front
        return prev
# time complexiy - O(n) and space compexity - O(1)