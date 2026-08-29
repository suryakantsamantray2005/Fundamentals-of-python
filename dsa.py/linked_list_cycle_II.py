#Linked list cycle II leetcode 142
class Solution:
    def detectCycle(self, head):
        slow=head
        fast=head
        temp=None
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                temp=slow
                break
        if temp==None:
            return None
        starting=head
        while starting is not None and starting.next is not None:
            if temp==starting:
                return temp
            else:
                temp=temp.next
                starting=starting.next
        return None
# time complexity - O(n) and space compelxity - O(1)