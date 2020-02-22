class Solution(object):
    def dominateIndex(self, nums):
        m = max(nums)
        if all(m >= 2*x for x in nums if x != 0):
            return nums.index(m)
        return -1