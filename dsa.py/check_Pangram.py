# check pangram leetcode 1832
class Solution:
    def checkIfPangram(self,sentence):
        if len(sentence)<26:
            return False
        else:
             S=set(sentence)
             if len(S)<26:
                 return False
             else:
              for i in S:
                 if 97>ord(i)<122:
                     return False
        return True
# time complexity - O(n) and space complexity - O(1)
obj=Solution()
print(obj.checkIfPangram("jwtucoucmdfwxxqnxzkaxoglszmfrcvjoiunqqausaxxaaijyqdqgvdnqcaihwilqkpivenpnekioyqujrdrovqrlxovcucjqzjsxmllfgndfprctxvxwlzjtciqxgsxfwhmuzqvlksyuztoetyjugmswfjtawwaqmwyxmvo"))