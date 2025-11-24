class Solution(object):
    def plusOne(self, digits):
        num = int("".join(map(str, digits)))
        
        num += 1
        
        
        result = [int(x) for x in str(num)]
        
        return result
