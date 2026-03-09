class Solution(object):
    def findRestaurant(self, list1, list2):
        result = []
        min_sum = 10000
        
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    if i + j < min_sum:
                        result = [list1[i]]
                        min_sum = i + j
                    elif i + j == min_sum:
                        result.append(list1[i])
        
        return result