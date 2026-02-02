class Solution(object):
    def sortedSquares(self, nums):
        arr=[]
        for x in nums:
            arr.append(x*x)
        arr.sort()
        return arr
       

        """
        :type nums: List[int]
        :rtype: List[int]
        """
        