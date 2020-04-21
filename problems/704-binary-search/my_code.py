# Accepted

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        head = 0
        tail = len(nums) - 1
        while head <= tail:
            center = (head + tail) // 2
            if nums[center] == target:
                return center
            elif nums[center] < target:
                head = center + 1
            else:
                tail = center - 1
        else:
            return -1
