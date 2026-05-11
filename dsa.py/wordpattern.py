#word pattern
class Solution:

    def wordPattern(self, pattern, s):
        words = s.split()

        my_dict = {}

        for ch, word in zip(pattern, words):
            my_dict[ch] = word

        return my_dict

obj = Solution()
print(obj.wordPattern("abab", "dog cat dog cat"))