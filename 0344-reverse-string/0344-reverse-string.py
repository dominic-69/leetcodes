class Solution(object):
    def reverseString(self, g):
        lest = 0
        right = len(g)-1
        while lest < right:
            g[lest],g[right]=g[right],g[lest]
            lest += 1
            right -= 1
        
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        