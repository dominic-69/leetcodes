class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for n in nums:
            if  n % 3 != 0:
                count +=1

        return count

       
        