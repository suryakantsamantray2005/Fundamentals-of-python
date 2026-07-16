# rotate string leetcode 796
class Solution:
    def rotateString(self, s, goal):
        if s==goal:
            return True
        result=s+s
        if goal in result:
            return True
        return False
# time complexity - O(n) and space compelxity - O(n)