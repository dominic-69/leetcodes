class Solution(object):
    def toLowerCase(self, s):
        new = ""
        for i in s:
            new += i.lower()
        return new
        """
        :type s: str
        :rtype: str
        """
        