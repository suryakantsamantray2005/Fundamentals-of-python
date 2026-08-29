# Delete the middle node of the linked list
class Solution:
    def deleteMiddle(self, head):
        if head.next==None:
            return None
        dummy=ListNode(0)
        dummy.next=head
        slow=dummy
        fast=head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
        slow.next=slow.next.next
        return head
# time comeplxity - O(n) and space complexity - O(1)