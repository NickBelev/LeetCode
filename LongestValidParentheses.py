class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_streak = 0 # Maximum length substring of valid parentheses

        # Count left and right parentheses encountered
        l_counter, r_counter = 0, 0

        # L -> R catches mismatches caused by too many )
        for i in range(len(s)):
            if s[i] == '(':
                l_counter += 1
            elif s[i] == ')':
                r_counter += 1
            
            if l_counter == r_counter:
                max_streak = max(max_streak, l_counter * 2)
                # We created a valid enclosure of parentheses, see if its length
                # is longer than the previous max and store it, if so
            elif r_counter > l_counter: # Closed more parentheses than we opened
                l_counter, r_counter = 0, 0 # Reset as we broke the streak

        # Note that this approach always underestimates total pairs / streak in one 
        # direction but correctly finds it in the other, with greater value, 
        # so it is ok to reuse max_streak in both directions

        # We can also have too many (, so must read R -> L 
        l_counter, r_counter = 0, 0

        # L -> R catches mismatches caused by too many )
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ')':
                r_counter += 1
            elif s[i] == '(':
                l_counter += 1
            
            if l_counter == r_counter:
                max_streak = max(max_streak, l_counter * 2)
                # We created a valid enclosure of parentheses, see if its length
                # is longer than the previous max and store it, if so
            elif l_counter > r_counter: # Opened more parentheses than we closed
                l_counter, r_counter = 0, 0 # Reset as we broke the streak


        return max_streak

