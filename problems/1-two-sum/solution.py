# solution
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        1. add each element's value and its index to the hash table.
        2. check if (target - nums[i]) exists in the table
        """
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]

# time complexity: O(n)
# space complexity: O(n)