# sorted array to bst | leetcode 108 | https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# given a sorted array of int, convert it to a balanced binary search tree
# method: take middle element as root, use recursion for depth first, add each subtree as a balanced bst

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        
        mid = len(nums) // 2
        
        root = TreeNode(val = nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        
        return root