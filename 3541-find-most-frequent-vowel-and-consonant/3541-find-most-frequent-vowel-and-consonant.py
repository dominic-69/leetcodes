class Solution:
    def maxFreqSum(self, s):
        vowels = "aeiou"
        v = c =0
        
        for ch in vowels:
            v = max(v,s.count(ch))
        
        for ch in s:
            if ch not in vowels:
                c =max(c, s.count(ch))
        
        return v + c
