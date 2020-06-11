import unittest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def toString(self):
        return f"{str(self.val)}{self.next.toString() if self.next != None else ''}"

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:       
        l3 = ListNode()
        head = l3
        c = 0
        while (l1 != None or l2 != None or c != 0):
            left = l1.val if l1 != None else 0
            right = l2.val if l2 != None else 0
            l3.next = ListNode((left + right + c) % 10)
            c = (left + right + c) // 10
            l1 = l1.next if l1 != None else None
            l2 = l2.next if l2 != None else None
            l3 = l3.next
            
        return head.next

class TestSolution(unittest.TestCase):
    def test_case1(self):
        l1 = ListNode(9, ListNode(9, ListNode(9)))
        l2 = ListNode(8)
        solution = Solution()
        self.assertEquals(solution.addTwoNumbers(l1, l2).toString(), "7001")


if __name__ == "__main__":
    unittest.main()