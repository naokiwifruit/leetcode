# Time Limit Exceeded

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_sum = 0
        for i, left in enumerate(prices):
            prices_ = [v for j, v in enumerate(prices) if j > i]
            for right in prices_:
                curr_sum = right - left
                if curr_sum > max_sum:
                    max_sum = curr_sum 
        
        return max_sum
