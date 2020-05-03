# Return the root node of a binary search tree that matches the given preorder traversal.

# (Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

# It's guaranteed that for the given test cases there is always possible to find a binary search tree with the given requirements.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        
        current = root
        stack = [root]        
        i = 1
        
        while i < len(preorder):
            if preorder[i] < current.val:
                current.left = TreeNode(preorder[i])
                current = current.left                
            else:
                while True:
                    if not stack or stack[-1].val > preorder[i]:
                        break
                    current = stack.pop()
                current.right = TreeNode(preorder[i])
                current = current.right
            stack.append(current)
            i += 1
            
        return root