class Solution(object):
    def countSeniors(self, details):
        """
        :type details: List[str]
        :rtype: int
        """
        new = 0
        
        for i in details:
            age = int(i[11:13])
            if age > 60:
                new += 1
                
        return new