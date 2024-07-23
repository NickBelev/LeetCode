class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Trivial case
        if len(s) == 0:
            return 0

        max_len = 1 # The max length must be at least 1 at this point
        
        # Left index for sliding window
        l = 0

        # dictionary to track letters and what index they occur at most recently
        chars = {}

        # Right index for sliding window
        for r in range(len(s)):
            # if we've already encountered s[r], within the bounds of l:r
            # set l to the index after s[r] occurred
            if s[r] in chars and chars[s[r]] >= l:
                l = chars[s[r]] + 1
            chars[s[r]] = r # Update the new occurrence of s[r] for future potential
            # window shrinkage / moving l

            # See if the current span of the substring is an improvement
            max_len = max(max_len, (r - l + 1))
        
        return max_len
