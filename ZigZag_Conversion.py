class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s # Edge case

        lines = []
        for i in range(numRows):
            lines.append([]) # Creating a 2D array with numRows rows


        curr_row = 0
        down = True # True for 0->n ++, False for n->0 --

        for ch in s: # current character
            lines[curr_row].append(ch)

            if curr_row == numRows - 1 and down:
                down = False # We reached the bottom row, start climbing back up
            if curr_row == 0 and not down:
                down = True # Reached the 0th row, start going back down

            if down:
                curr_row += 1 # We've still got room to count up
            else:
                curr_row -= 1

        result = ""

        for line in lines:
            for ch in line:
                result += ch
        
        return result

            
