# Linked list cycle leetcode 141
# Floyd's Cycle Detection Algorithm also called tortoise and hare algorithm
class Solution:
    def hasCycle(self, head):
        slow=head
        fast=head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False
# time complexity - O(n) and space complexity - O(1)