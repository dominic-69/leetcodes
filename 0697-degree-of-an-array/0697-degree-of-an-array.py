class Solution:
    def findShortestSubArray(self, nums):
        data ={}
        
        for i, n in enumerate(nums):
            if n not in data:
                data[n]=[1,i,i] 
            else:
                data[n][0] += 1
                data[n][2] = i

        degree= max(v[0] for v in data.values())
        ans =len(nums)

        for count,first,last in data.values():
            if count ==degree:
                ans= min(ans,last - first +1)

        return ans
