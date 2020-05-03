# Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

# Example 1:
# Input:nums = [1,1,1], k = 2
# Output: 2


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        current_sum = 0
        hash_map = {}
        hash_map[0] = 1
        
        for num in nums:
            current_sum += num
            if hash_map.get(current_sum - k):
                count += hash_map[current_sum - k]
            hash_map[current_sum] = hash_map.get(current_sum, 0) + 1
            
        return count