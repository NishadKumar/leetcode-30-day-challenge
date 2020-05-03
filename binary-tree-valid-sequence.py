# Given a binary tree where each path going from the root to any leaf form a valid sequence, check if a given string is a valid sequence in such binary tree. 

# We get the given string from the concatenation of an array of integers arr and the concatenation of all values of the nodes along a path results in a sequence in the given binary tree.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidSequence(self, root, arr):
        """
        :type root: TreeNode
        :type arr: List[int]
        :rtype: bool
        """
        return self.isValid(root, arr, 0)
    
    def isValid(self, node, arr, index):
        
        if node.val != arr[index]:
            return False
        
        if index == len(arr) - 1: 
            return not node.left and not node.right
        
        if node.left and self.isValid(node.left, arr, index + 1):
            return True
        
        if node.right and self.isValid(node.right, arr, index + 1):
            return True
        
        return False