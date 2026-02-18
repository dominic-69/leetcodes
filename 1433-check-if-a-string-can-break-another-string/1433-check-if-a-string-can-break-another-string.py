class Solution(object):
    def checkIfCanBreak(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
 
        s1 = sorted(s1)
        s2 = sorted(s2)
        a = True
        b = True
        for i in range(len(s1)):
            if s1[i]<s2[i]:
                a = False
            if s1[i]>s2[i]:
                b = False
        
        return a or b
