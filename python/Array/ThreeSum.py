from typing import List
import unittest

class Solution(unittest.TestCase):
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result, length = [], len(nums)
        nums.sort()

        for i in range(length - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, length - 1

            while left < right:

                if nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left, right = left + 1, right - 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return result

    def test_case1(self):
        self.assertEqual(self.threeSum([0, 0, 0, 0]), [[0, 0, 0]])

if __name__ == "__main__":
    unittest.main()