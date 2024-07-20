class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]] # The base case of PT has 1 row of just the number 1

        # First loop in charge of piecing together the triangle
        # We've already done 1 row so need the remaining numRows - 1
        for i in range(numRows - 1):
            # Previous row to current one, with 0's appended to the ends for 
            # consisting adding of adjacent terms to make the next row
            prev_row = [0] + triangle[len(triangle) - 1] + [0]
            new_row = []

            # add together every adjacent pair of terms and 
            # add the result to the new row
            for j in range (0, len(prev_row) - 1):
                new_row.append(prev_row[j] + prev_row[j + 1])
            
            # new row is finished, so add it to the list of all rows
            triangle.append(new_row)
        return triangle # triangle has correct number of completed rows
