class Solution(object):
    def maximumWealth(self, accounts):
        max_wealth = 0
        for customer in accounts:
            current_wealth=sum(customer)
            if current_wealth > max_wealth:
                max_wealth =current_wealth
        return max_wealth
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        