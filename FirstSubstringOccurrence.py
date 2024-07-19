class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i, ch in enumerate(haystack):
            # If our iteration leaves outstanding fewer characters
            # than there are in the needle we're looking for
            # the needle cannot be there and we want to avoid index out of 
            # bounds, so we break
            if i > (len(haystack) - len(needle)):
                # Ex. aa in zzzz
                # i > ((4 - 2) = 2) => i >= 3 => zzzz
                # Not enough space for aa          i^ 
                break

            # Preliminary check if current character is same as 
            # starting character of the needle
            if ch == needle[0:1]:
                # Secondary check for equality:
                # Is substring of haystack from i
                # up to the length of the string needle 
                # equal to the needle?
                if haystack[i:(i + len(needle))] == needle:
                    return i # If so, we've found our first satisfactory index
        return -1 # Didn't find needle in the haystack, else would've been caught above
