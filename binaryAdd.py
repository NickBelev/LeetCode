class Solution:
    def addBinary(self, a: str, b: str) -> str:

        # Edge case since we start with an empty string
        # And for non-zero numbers we skip adding a 0 
        # in front once we've reached the 0th index
        if a == "0" and b == "0":
            return "0"

        # Initialize carry holder which will always be 0 or 1
        carry = 0
        res = "" # To store the sum

        # Ends of both numbers
        a_index = len(a) - 1
        b_index = len(b) - 1
        
        # We work backwards from the end of each number
        # Lined up against each other, like grade school addition
        # Loop ends when the smaller of the two numbers runs out of digits
        while a_index >= 0 and b_index >= 0:
            # 1 + 1 w/ carry
            if (int(a[a_index]) + int(b[b_index]) + carry) == 3:
                carry = 1
                res = "1" + res
            # 1 + 1 OR 1 + 0 w/ carry
            elif (int(a[a_index]) + int(b[b_index]) + carry) == 2:
                carry = 1
                res = "0" + res
            # 1 + 0 OR carry
            elif (int(a[a_index]) + int(b[b_index]) + carry) == 1:
                carry = 0
                res = "1" + res
            # all 0's
            elif a_index != 0 or b_index != 0: # No need for 0 at front of number
                carry = 0
                res = "0" + res
            
            # decrement indices
            a_index -= 1
            b_index -= 1

        # If a is out of digits, this will be skipped over
        while a_index >= 0:
            # 1 w/ carry
            if (int(a[a_index]) + carry) == 2:
                carry = 1
                res = "0" + res
            # 1 OR carry
            elif (int(a[a_index]) + carry) == 1:
                carry = 0
                res = "1" + res
            # all 0's
            elif a_index != 0: # No need for 0 at front of number
                carry = 0
                res = "0" + res

            a_index -= 1


        # If b is out of digits, this will be skipped over
        while b_index >= 0:
            # 1 w/ carry
            if (int(b[b_index]) + carry) == 2:
                carry = 1
                res = "0" + res
            # 1 OR carry
            elif (int(b[b_index]) + carry) == 1:
                carry = 0
                res = "1" + res
            # all 0's
            elif b_index != 0: # No need for 0 at front of number
                carry = 0
                res = "0" + res

            b_index -= 1
        
        # Final operation led to a carry, exceeding bits of the larger number
        if carry == 1:
            res = "1" + res

        return res
