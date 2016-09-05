class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(reversed(s.split()))

a = Solution()


print a.reverseWords('columbia university in the city of new york')

