class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Essentially grade school multiplication algorithm
        total = 0

        # Tracking trailing 0's due to going into the higher digits of num1
        mult1 = 1
        for i in range(len(num1) - 1, -1, -1):
            # Tracking trailing 0's due to going into the higher digits of num2
            mult2 = 1
            for j in range(len(num2) - 1, -1, -1):
                # Casting digits to int and incrementing their corresponding
                # product (with correct number of trailing 0's) to the result
                total += mult1 * mult2 * int(num1[i]) * int(num2[j])
                mult2 *= 10
            mult1 *= 10
        
        return str(total)
