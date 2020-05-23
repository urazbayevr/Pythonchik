"""class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:

        ans = 0

        def rec(root, L, R):
            nonlocal ans
            if root:
                if L <= root.val <= R:
                    ans += root.val

                if L < root.val:
                    rec(root.left, L, R)
                if R > root.val:
                    rec(root.right, L, R)

        rec(root, L, R)
        return ans

s = Solution()
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if root is None:
            return 0

        return (
                self.rangeSumBST(root.left, L, R) +
                self.rangeSumBST(root.right, L, R) +
                (root.val if L <= root.val <= R else 0)
        )


def buildTree(a: list):
    '''
    build tree from list
    '''
    root = TreeNode(a[0])
    tree = [root]

    # index from 1
    # skip first element, a[1:]
    for i, val in enumerate(a[1:], 1):
        if val is not None:
            new_node = TreeNode(val)

            # get parent node's index
            p_i = (i - 1) // 2

            if i % 2 == 1:
                tree[p_i].left = new_node
            else:
                tree[p_i].right = new_node

            tree.append(new_node)
        else:
            tree.append(None)

    return root


arr = [10, 5, 15, 3, 7, None, 18]

# visualization: (index: value)
#
#                   (0: 10)
#        (1: 5)                 (2: 15)
#   (3: 3)   (4: 7)     (5: null)     (6: 18)


# input data
L = 7
R = 15
root = buildTree(arr)

sol = Solution()
print(sol.rangeSumBST(root, L, R))