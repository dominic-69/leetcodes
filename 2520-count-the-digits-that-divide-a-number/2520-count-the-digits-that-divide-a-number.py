class Solution(object):
    def countDigits(self, num):
        nums = str(num)
        count = 0 
        for i in  nums:
            digit=int(i)
            if num % digit == 0:
                count +=1 



            
        return count
        """
        :type num: int
        :rtype: int
        """
        