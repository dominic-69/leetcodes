class Solution(object):
    def differenceOfSums(self, n, m):
        yes = 0
        no =0
        
        for i in range(1,n + 1):
            if i % m == 0:
                yes += i
            else:
                no += i
                
        return no - yes