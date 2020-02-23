class Solution(object):
    def dominateIndex(self, nums):
        m = max(nums)
        if all(m >= 2*x for x in nums if x != 0):
            return nums.index(m)
        return -1

        # time complexity: O(N) where N is the length of nums
        # space complexity: O(1), the space used by our int variables