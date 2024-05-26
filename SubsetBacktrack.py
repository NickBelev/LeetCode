class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [] # To store all possible subsets

        subset = [] # To make the current recursive subset

        # To create all possible subsets using inclusion and exclusion each 
        # element in every combination
        def backtrack(i):
            if i >= len(nums): # Done with this branch of recursion
                # Store the subset we ended up making
                subsets.append(subset.copy())
                return

            # Exclude ith element and continue recursion
            backtrack(i + 1)

            # Include ith element and continue recursion
            subset.append(nums[i])
            backtrack(i + 1)
            subset.pop() # Unstack the last element to explore alternative (ie. 
                         # not including it), do this after each inclusion
                         # else, we'll end up stacking together subsets larger
                         # than the original set.

        # Backtrack on the input list
        backtrack(0)
        return subsets # Done
