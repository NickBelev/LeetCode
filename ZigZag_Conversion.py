class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        canvas = ['' for _ in range(numRows)]
        y, direction = 0, 1

        for ch in s:
            canvas[y] += ch
            if y == 0:
                direction = 1
            elif y == numRows - 1:
                direction = -1
            y += direction

        return ''.join(canvas)

