class Solution:
    def countAndSay(self, n: int) -> str:
        # start with base case
        rle = curr_ch = "1" # We always start from 1

        # create RLE "memoization"
        for i in range(n - 1): # Don't run if n = 1
            rle2 = ""
            count = 1
            for j in range(1, len(rle)):
                if rle[j - 1] == rle[j]:
                    count += 1
                else:
                    rle2 += str(count) + rle[j - 1]
                    count = 1
            
            rle2 += str(count) + rle[len(rle) - 1]            
            rle = rle2 # fully constructed the ith countAndSay number, save it, and calculate the i+1th number using the ith as a starting point

        return rle
