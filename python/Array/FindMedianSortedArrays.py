from typing import List
import unittest
import sys

class Solution:

    # based on position find the position from 0 - 2*n, which half of the numbers are smaller than right
    def findMedianSortedArrays(self, a1: List[int], a2: List[int]) -> float:
        nums1, nums2 = sorted([a1, a2], key=len)

        len1 = len(nums1)
        len2 = len(nums2)
        left = 0
        right = 2 * len1

        while left <= right:
            p1 = (left + right) // 2
            p2 = len1 + len2 - p1

            leftValue1 = -sys.maxsize if p1 < 1 else nums1[(p1 - 1) // 2]
            rightValue1 = sys.maxsize if p1 >= 2*len1 else nums1[p1 // 2]
            leftValue2 = -sys.maxsize if p2 < 1 else nums2[(p2 - 1) // 2]
            rightValue2 = sys.maxsize if p2 >= 2*len2 else nums2[p2 // 2]

            if leftValue1 <= rightValue2 and leftValue2 <= rightValue1:
                return (max(leftValue1, leftValue2) + min(rightValue1, rightValue2)) / 2
            elif leftValue1 > rightValue2:
                right = p1 - 1
            else:
                left = p1 + 1

    # instead of using position, find the smallest (m + n -1) / 2 numbers
    # based on the total length, the mdeian can be one number or a half from the smallest 2 numbers in the middle
    def findMedianSortedArrays2(self, a1: List[int], a2: List[int]) -> float:
        nums1, nums2 = sorted((a1, a2), key=len)

        m, n = len(nums1), len(nums2)

        smallHalf = (m + n - 1) // 2
        left, right = 0, m

        while left < right:
            i = (left + right) // 2
            j = smallHalf - i

            condition1 = j == 0 or (nums1[i] > nums2[j - 1])
            condition2 = i == 0 or (nums2[j] > nums1[i - 1])

            if condition1 and condition2:
                left = i
                break
            elif not condition1:
                left = i + 1
            else:
                right = i
        
        i = left
        j = smallHalf - left

        # slice will hande the edge case well
        middleNumbers = sorted(nums1[i:i + 2] + nums2[j:j + 2])
        return (middleNumbers[0] + middleNumbers[1 - (m + n) % 2]) / 2



class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_case1(self):
        self.assertEqual(self.solution.findMedianSortedArrays2([2,3], [1]), 2)

    def test_case2(self):
        self.assertEqual(self.solution.findMedianSortedArrays2([1,2], [-1,3]), 1.5)
if __name__ == "__main__":
    unittest.main()