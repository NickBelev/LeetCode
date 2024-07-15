class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Initialize a backtracking list to save previous results and work bottom-up
        dynamicMem = [False] * (len(s) + 1)
        # Base case, the empty end of the string can always be made using the empty substring
        dynamicMem[len(s)] = True 
        
        # Iterate from end to beginning of the string
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                # Enough characters to check for match while staying in bounds
                # Compare substrings with each possible word in the dictionary
                if (i + len(w) <= len(s)) and (s[i:i + len(w)] == w):
                    # Found a match, somewhere in the word
                    # Use previous results to know if the entire string i:end is formable via words from the dictionary
                    dynamicMem[i] = dynamicMem[i + len(w)]

                if dynamicMem[i]:
                    break
                    # We found one word that allows for i:end to be formable
                    # So let's move on

        return dynamicMem[0] # Once we've worked up to the beginning of the string, our solution is dictated by whether 0:end is formable using words from the dictionary, so return just that
