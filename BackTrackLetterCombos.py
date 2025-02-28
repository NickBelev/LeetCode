class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return [] # Empty digits ==> no possible combos - edge case
        
        digit_vals = { 
            # Map of digits to their each of their letters, as a list
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        combos = [] # to store combinatorial results

        def combinations(index, curr_combo):
            if index == len(digits): 
                # If we've recursively reached the last digit in the string
                combos.append("".join(curr_combo)) # we've constructed one 
                # possible combination, so add it to return list, this 
                # terminates the recursion in line 30 at every level.
                return
            
            for letter in digit_vals[digits[index]]: # DFS
                curr_combo.append(letter) # step along the current combo
                combinations(index + 1, curr_combo) # move onto next step
                curr_combo.pop()  # backtrack the priorly added letter 
                # (after the recursion line above reached the end aka made a 
                # full combination), then try another letter value for the 
                # current digit
        
        combinations(0, []) # Start at index zero with no pre-formed combos
        return combos # Return all the combos we could make
