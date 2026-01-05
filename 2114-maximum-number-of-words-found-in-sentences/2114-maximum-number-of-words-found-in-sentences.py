class Solution(object):
    def mostWordsFound(self, sentences):
        max_words= 0
        for i in sentences:
            count = len(i.split())
            if count > max_words:
                max_words=count
        return max_words
        """
        :type sentences: List[str]
        :rtype: int
        """
        