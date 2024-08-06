class Solution:
    def longestPalindrome(self, s: str) -> str:
        long_pal = "" # Default case, empty palindrome
        # long_len = 0 # Has length 0

        # Try every char in s as the center of a palindrome, optimal solution
        for i in range(len(s)):
            l, r = i, i # bound pointers from i, the center of the palindrome
            # for odd length palindromes
            while l >= 0 and r < len(s) and s[l] == s[r]: 
                # Bounds of the string and remains palindromic while expanding the
                # substring each iteration
                if (r - l + 1) > len(long_pal): #long_len:
                    #long_len = (r - l + 1) # Found a longer palindrome
                    long_pal = s[l:r + 1] # This is it
                
                # Expand both pointers by 1, keeping palindrome length odd
                l -= 1
                r += 1

            l, r = i, i + 1 # bound pointers from i, the middle pair palindrome
            # for even length palindromes
            while l >= 0 and r < len(s) and s[l] == s[r]: 
                # Bounds of the string same as before
                if (r - l + 1) > len(long_pal): #long_len:
                    # long_len = (r - l + 1) # Found a longer palindrome
                    long_pal = s[l:r + 1] # This is it
                
                # Expand both pointers by 1, keeping palindrome length even
                l -= 1
                r += 1
            
            # So we find the better of even and odd length palindromes where i
            # (and/or i+1) is in the center for each palindrome substring of s
            # long_pal thus stores the best final result

        return long_pal
