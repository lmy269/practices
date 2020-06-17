import unittest

class Solution(unittest.TestCase):
    cache = {}

    def numTrees(self, num: int) -> int:
        totalSum = 0
        if num == 0:
            return 1
        if num in self.cache:
            return self.cache[num]
        for i in range(num):
            totalSum += self.numTrees(i) * self.numTrees(num - 1 - i)

        self.cache[num] = totalSum
        return totalSum

    def numTrees2(self, num: int) -> int:
        res = [0] * (num + 1)

        res[0] = 1

        for i in range(1, num + 1):
            for j in range(0, i):
                res[i] += res[j] * res[i - j - 1]

        return res[num]

    def test_case1(self):
        self.assertEqual(self.numTrees(3), 5)

    def test_case2(self):
        self.assertEqual(self.numTrees2(3), 5)

if __name__ == "__main__":
    unittest.main()