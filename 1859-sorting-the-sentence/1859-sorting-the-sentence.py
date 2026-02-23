class Solution(object):
    def sortSentence(self, s):
        word = s.split()
        result = [""] * len(word)
        for i in word:
            index =int(i[-1]) -1
            result[index] = i[:-1] 
        return " ".join(result)


        """
        :type s: str
        :rtype: str
        """
        