# Run Code: Accepted
# Submit: Wrong Answer

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return sum(nums)
        
        max_sum = 0
        for left_idx, left in enumerate(nums):
            for right_idx, right in enumerate(nums):
                cont_sum = sum(nums[left_idx+1:right_idx])
                if cont_sum > max_sum:
                    max_sum = cont_sum
                    
        return max_sum
       
