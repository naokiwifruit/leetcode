# Wrong Answer

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i, num in enumerate(nums):
            if num == 0:
                for j in range(len(nums)-i-1):
                    nums[i+j] = nums[i+j+1]
                nums[-1] = 0
