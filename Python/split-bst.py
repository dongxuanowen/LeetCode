# Time:  O(n)
# Space: O(h)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def splitBST(self, root, V):
        """
        :type root: TreeNode
        :type V: int
        :rtype: List[TreeNode]
        """
        if not root:
            return None, None
        elif root.val <= V:
            result = self.splitBST(root.right, V)
            root.right = result[0]
            return root, result[1]
        else:
            result = self.splitBST(root.left, V)
            root.left = result[1]
            return result[0], root
