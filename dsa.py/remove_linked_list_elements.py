# Remove the linked list elements leetcode 203
class Solution:
    def removeElements(self, head, val):
        temp=head
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy
        while temp is not None:
            if temp.val==val:
                if temp.next is None:
                    prev.next=None
                    temp=temp.next
                else:
                    temp.next.prev=prev
                    prev.next=prev.next.next
                    temp=temp.next
            else:
                temp=temp.next
                prev=prev.next
        return dummy.next
# time complexity - O(n) and space comeplxity - O(1)