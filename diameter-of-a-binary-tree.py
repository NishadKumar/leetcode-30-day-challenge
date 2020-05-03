# Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# Example:
# Given a binary tree
#           1
#          / \
#         2   3
#        / \     
#       4   5    
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

# Note: The length of path between two nodes is represented by the number of edges between them.

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.diameter(root)
    
    def diameter(self, node):
        if not node:
            return 0
        
        lheight = self.height(node.left)
        rheight = self.height(node.right)
        ldiameter = self.diameter(node.left)
        rdiameter = self.diameter(node.right)
        
        return max(lheight + rheight, max(ldiameter, rdiameter))
    
    def height(self, node):
        if not node:
            return 0
        
        lheight = self.height(node.left)
        rheight = self.height(node.right)
        
        return max(lheight, rheight) + 1