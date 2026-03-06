class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        return [sum(i in nums2 for i in nums1), sum(i in nums1 for i in nums2)]
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        