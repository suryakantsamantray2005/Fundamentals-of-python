# Remove nth Node from the end of the list leetcode 19
class  Solution:
    def removeNthFromEnd(self, head, n):
        temp=head
        count=0
        while temp is not None:
            count+=1
            temp=temp.next
        if count==n:
            temp=head
            head=head.next
            return head
        temp=head
        i=0
        while True:
            i+=1
            if count-i==n:
                break
            temp=temp.next
        temp.next=temp.next.next
        return head
# time comeplexity - O(n) and space complexity - O(1)