#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def height(root: TreeNode) -> int:
    if root == None:
        return 0
    leftHeight = height(root.left)
    rightHeight = height(root.right)
    if leftHeight == -1 or rightHeight == -1:
        return -1
    if abs(leftHeight - rightHeight) > 1:
        return -1
    return max(leftHeight, rightHeight) + 1

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        if height(root) == -1:
            return False
        return True
        
# @lc code=end

