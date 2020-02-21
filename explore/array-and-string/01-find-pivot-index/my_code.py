# accepted
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        S = sum(nums)
        leftsome = 0
        for i, num in enumerate(nums):
            if leftsome == S - num - leftsome:
                return i
            else:
                leftsome += num
        return -1