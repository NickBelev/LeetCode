class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31 # Good practice

        i = 0
        n = len(s) 

        # Skip leading whitespaces
        while i < n and s[i] == " ":
            i += 1

        # Check if string is empty after whitespace
        if i == n: # We reached the end of the number without finding a valid character
            return 0

        # Check sign
        negative = False
        if s[i] == '-':
            negative = True
            i += 1 # Skip over sign
        elif s[i] == '+':
            i += 1

        # Parse number
        num = 0
        while i < n and s[i].isdigit(): # Stop once we encounter non digit or reach end of string
            num = num * 10 + int(s[i]) # left shift curr number and append next rightmost digit
            i += 1 

        if negative:
            num = -num # Correct sign if needed

        # Restrict to 32-bit signed int range
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX

        return num # String has been converted to int
