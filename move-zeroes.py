# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Example:

# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Note:
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        first_pointer = 0
        second_pointer = 0
        
        while second_pointer < len(nums):
            if nums[second_pointer] != 0 :
                nums[first_pointer] = nums[second_pointer]
                first_pointer += 1
            second_pointer += 1
        
        while first_pointer < len(nums):
            nums[first_pointer] = 0
            first_pointer += 1
