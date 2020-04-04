# Time Limit Exceeded

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        for i in range(len(s)):
            if s[i] not in [char for idx, char in enumerate(s) if idx != i]:
                return i
        return -1
