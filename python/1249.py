# Problem 
# 1249: Minimum Remove To Make Valid Parentheses
# Remove minimum number of parentheses so that the resulting parentheses return a valid string
# input: s = "leet(c)o)de)"
# Expected Output: "leet(t(c)o)de" or "lee(t(c)ode)"


# Solution
class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        countOpenParentheses = 0
        arr = list(s)

        # Sieve Out Closing Parentheses 
        for i in range(len(arr)):
            if arr[i] == '(':
                countOpenParentheses += 1
            elif arr[i] == ')':
                if countOpenParentheses == 0:
                    # Mark excess closing parentheses 
                    arr[i] = '*' 
                else:
                    countOpenParentheses -= 1

        # Mark excess opening parameters 
        for i in range(len(arr) - 1, -1, -1):
            if countOpenParentheses > 0 and arr[i] == '(':
                arr[i] = '*'
                countOpenParentheses -= 1

        result = ''.join(c for c in arr if c != '*')

        return result


# Runtime 
# Time Complexity: O(n)
# Space Complexity: O(n)
# Runtime: 39ms
# Author: Kiprotich
