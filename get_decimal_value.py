# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        print(head)
        curr = ListNode(head)
        res = 0
        while (curr):
            res *= 2
            res += curr.val
            curr = curr.next
        return res

binary = [1,0,1]

s = Solution()

print(s.getDecimalValue(binary))