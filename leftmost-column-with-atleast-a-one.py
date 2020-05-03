# A binary matrix means that all elements are 0 or 1. For each individual row of the matrix, this row is sorted in non-decreasing order.

# Given a row-sorted binary matrix binaryMatrix, return leftmost column index(0-indexed) with at least a 1 in it. If such index doesn't exist, return -1.

# You can't access the Binary Matrix directly.  You may only access the matrix using a BinaryMatrix interface:

# BinaryMatrix.get(row, col) returns the element of the matrix at index (row, col) (0-indexed).
# BinaryMatrix.dimensions() returns a list of 2 elements [rows, cols], which means the matrix is rows * cols.
# Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer.  Also, any solutions that attempt to circumvent the judge will result in disqualification.

# For custom testing purposes you're given the binary matrix mat as input in the following four examples. You will not have access the binary matrix directly.

 
# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x, y):
#        """
#        :type x : int, y : int
#        :rtype int
#        """
#
#    def dimensions:
#        """
#        :rtype list[]
#        """

class Solution(object):
    def leftMostColumnWithOne(self, binaryMatrix):
        """
        :type binaryMatrix: BinaryMatrix
        :rtype: int
        """
        dimensions = binaryMatrix.dimensions() 
        least_column = sys.maxsize
        flag = False
        
        i = 0
        j = dimensions[1] - 1
        
        while i < dimensions[0] and j >= 0:
            if binaryMatrix.get(i, j) == 0:
                i += 1
            else:
                flag = True
                least_column = min(least_column, j)
                j -= 1
                    
        return least_column if flag else -1