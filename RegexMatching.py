class Solution:
    def isMatch(self, s: str, r: str) -> bool:
        states = {} # dictionary of (ps, pr) -> True / False (does this pairing yield a valid regex match)
        
        def search(ps, pr):
            if (ps, pr) in states:
                return states[(ps, pr)]
            if ps >= len(s) and pr >= len(r): # Both pointers reached end simultaneously, without failing; they match.
                return True
            if pr >= len(r):
                return False # reached past the end of the regex, cannot possibly match more letters.
            
            match = ps < len(s) and (s[ps] == r[pr] or r[pr] == '.')
            
            if (pr + 1 < len(r)) and r[pr + 1] == '*': # character after this one is *
                states[(ps, pr)] = (
                    search(ps, pr + 2) # one option is to see if a True is possible by using 0 occurrences of ps (skipping the *)
                    or # allows for one of these conditions being True to "bubble up" the True return
                    (match and search(ps + 1, pr)) # if current matches, try to match next character in s with same pattern (recursively we will again be aqble to choose to stop using the * or try with it again)
                    # All we care about is if one possible matching is valid.
                )
            
                return states[(ps, pr)]

            if match:
                states[(ps, pr)] = search(ps + 1, pr + 1) # onto next character comparison
                return states[(ps, pr)]
            
            return False # else character mismatch, or invalid character, strings cannot match.
        
        return search(0, 0)
