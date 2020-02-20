# my_code
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for fac1_idx, fac1 in enumerate(nums):
            for fac2_idx, fac2 in enumerate(nums):
                if fac1_idx != fac2_idx and fac1 + fac2 == target:
                    return [fac1_idx, fac2_idx]

# time complexity: O(n^2)