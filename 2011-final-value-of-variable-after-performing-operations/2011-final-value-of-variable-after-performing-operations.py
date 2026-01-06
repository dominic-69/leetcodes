class Solution(object):
    def finalValueAfterOperations(self, operations):
        return sum(1 if '+' in jk else -1 for jk in operations)
        """
        :type operations: List[str]
        :rtype: int
        """
        