# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    def deepestLeavesSum(self, root):
        frontier = [root]
        res = 0
        while frontier:
            temp = []
            res = 0
            for n in frontier:
                res += n.val
                if n.left: temp += [n.left]
                if n.right: temp += [n.right]
            frontier = temp
        return res

root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
s = Solution()
print(s.deepestLeavesSum(root))