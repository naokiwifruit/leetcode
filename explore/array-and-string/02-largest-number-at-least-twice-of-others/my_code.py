class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        biggest_idx = 0
        second_idx = 0
        for i, num in enumerate(nums):
            if num > nums[biggest_idx]:
                second_idx = biggest_idx
                biggest_idx = i
        if nums[biggest_idx] >= 2 * nums[second_idx]:
            return biggest_idx
        else:
            return -1

        # Wrong Answer