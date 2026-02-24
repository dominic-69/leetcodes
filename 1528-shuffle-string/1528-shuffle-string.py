class Solution(object):
    def restoreString(self, s, indices):
        reslt =[""]*len(s)
        for i in range (len(s)):
            reslt [indices[i]] =s[i]
        return "".join(reslt)
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        