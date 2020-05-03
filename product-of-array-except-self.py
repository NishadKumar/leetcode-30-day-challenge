# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

# Example:

# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

# Note: Please solve it without division and in O(n).

# Follow up:
# Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        left_product = [0] * len(nums)
        right_product = [0] * len(nums)
        
        for i in range(len(nums)):
            if i == 0:
                left_product[i] = 1
            else:
                left_product[i] = left_product[i-1] * nums[i-1]
        
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                right_product[i] = 1
            else:
                right_product[i] = right_product[i+1] * nums[i+1]
        
        return [left_product[i] * right_product[i] for i in range(len(nums))]