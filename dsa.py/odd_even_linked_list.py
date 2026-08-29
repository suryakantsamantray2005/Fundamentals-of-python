# Odd even linked list leetcode 328
class Solution:
    def oddEvenList(self, head):
        if head is None:
            return head
        odd=head
        even=head.next
        even_head=head.next
        while odd.next is not None and even.next is not None:
            odd.next=odd.next.next
            even.next=even.next.next
            odd=odd.next
            even=even.next
        odd.next=even_head
        return head
# time complexity - O(n) and space complexity - O(1)