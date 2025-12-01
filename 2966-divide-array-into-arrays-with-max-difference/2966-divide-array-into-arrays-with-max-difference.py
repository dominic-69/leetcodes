class Solution(object):
    def divideArray(self, nums, k):
        
        nums.sort()
        n=len(nums)
        res=[]
        for i in range(2, n, 3):
            if nums[i] -nums[i-2]>k:
                return[]
            res.append([nums[i-2],nums[i-1],nums[i]])

        return res
