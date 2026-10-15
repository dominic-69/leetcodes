class Solution(object):
    def maxArea(self, height):
        l = 0
        r = len(height) - 1
        ans = 0
        
        while l < r:
            w = r - l
            # find min height manually
            h = height[l]
            if height[r] < h:
                h = height[r]
                
            vol = w * h
            if vol > ans:
                ans = vol
            
            # move the smaller one
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
                
        return ans