class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}
        t_to_s = {}

        for char_s, char_t in zip(s, t):
            # If we've encountered X in s and X' in t, then ensure that:
            # Every time X appears in s, X' appears in t,
            # Every time X' appears in t, X appears in s.
            if (char_s in s_to_t and s_to_t[char_s] != char_t) or (char_t in t_to_s and t_to_s[char_t] != char_s):
                return False

            # If X, X' weren't in the dictionaries add them
            # If X or X' now has a different value, change it
            # This will reveal a future conflict later since
            # only one mapping will be different for X / X'
            s_to_t[char_s] = char_t
            t_to_s[char_t] = char_s

        return True
