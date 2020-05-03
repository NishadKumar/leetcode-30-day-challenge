# Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
# An empty string is also valid.


# Example 1:
# Input: "()"
# Output: True

# Example 2:
# Input: "(*)"
# Output: True

# Example 3:
# Input: "(*))"
# Output: True

class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s or s == "*":
            return True
        
        if len(s) == 1:
            return False
        
        left_brackets = 0
         
        for character in s:
            if character == ')':
                left_brackets -= 1
            else:
                left_brackets += 1
                
            if left_brackets < 0:
                return False
            
        if left_brackets == 0:
            return True
        
        right_brackets = 0
        
        for character in reversed(s):
            if character == '(':
                right_brackets -= 1
            else:
                right_brackets += 1
                
            if right_brackets < 0:
                return False
        
        return True

