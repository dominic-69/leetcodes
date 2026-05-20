class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        C =[]
        set_A =set()
        set_B =set()
        
        for i in range(len(A)):
            set_A.add(A[i])
            set_B.add(B[i])
            common_count=len(set_A.intersection(set_B))
            C.append(common_count)
            
        return C
        
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        