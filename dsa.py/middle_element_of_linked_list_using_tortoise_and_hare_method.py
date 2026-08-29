# middle ellemt of the linked list using the tortoise and hare method
class Solution:
    def middleNode(self, head):
        slow=head
        fast=head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
        return slow
# time complexity - O(n) and space complexity - O(1)