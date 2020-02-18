class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lower_bound = 0
        upper_bound = len(nums) - 1

        while upper_bound >= lower_bound:
            index = int((lower_bound + upper_bound) / 2)
            if target == nums[index]:
                return index
            if target > nums[index]:
                lower_bound = index + 1
            else:
                upper_bound = index - 1

        return -1