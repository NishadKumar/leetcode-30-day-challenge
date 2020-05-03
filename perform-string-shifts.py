# You are given a string s containing lowercase English letters, and a matrix shift, where shift[i] = [direction, amount]:

# direction can be 0 (for left shift) or 1 (for right shift). 
# amount is the amount by which string s is to be shifted.
# A left shift by 1 means remove the first character of s and append it to the end.
# Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.
# Return the final string after all operations.

 

# Example 1:

# Input: s = "abc", shift = [[0,1],[1,2]]
# Output: "cab"
# Explanation: 
# [0,1] means shift to left by 1. "abc" -> "bca"
# [1,2] means shift to right by 2. "bca" -> "cab"
# Example 2:

# Input: s = "abcdefg", shift = [[1,1],[1,1],[0,2],[1,3]]
# Output: "efgabcd"
# Explanation:  
# [1,1] means shift to right by 1. "abcdefg" -> "gabcdef"
# [1,1] means shift to right by 1. "gabcdef" -> "fgabcde"
# [0,2] means shift to left by 2. "fgabcde" -> "abcdefg"
# [1,3] means shift to right by 3. "abcdefg" -> "efgabcd"


class Solution(object):
    def stringShift(self, s, shift):
        """
        :type s: str
        :type shift: List[List[int]]
        :rtype: str
        """
        actual_shifts = self.calculate_shifts(shift)
        
        if actual_shifts:
            return self.perform_shift(s, actual_shifts)
        
        return s
        
    def calculate_shifts(self, shifts):
        total = 0
        
        for shift in shifts:
            if shift[1]:
                if shift[0] == 1:
                    shift[1] *= -1
                total += shift[1]
        return total
    
    def perform_shift(self, s, actual_shifts):
        
        actual_shifts %=  len(s)
        
        first = s[ :actual_shifts] 
        second = s[actual_shifts: ]
        
        return second + first