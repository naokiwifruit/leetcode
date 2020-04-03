class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero_idx = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero_idx] = nums[zero_idx], nums[i]
                zero += 1
                
# Space Complexity: O(1)
# Time Complexity: O(n)
