class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        # Base recursive case, the list of permutations of a single element list
        # only has one element within it, that same single element list
        if len(nums) == 1:
            return [nums]

        # For the current recursive sub problem, always start with an empty
        # list of currently collected permutations.  As we recurse back up
        # To build the bigger problem we'll return the perms of all subproblems
        # To build the bigger lists by including a fixed element at the front of
        # each list
        perms = []

        # For every num in nums, fix the place of the current num to the beginning 
        # of each permutation list. Doing so for every num will cover all orders
        for i in range(len(nums)):
            curr = nums[i]
            # The list, excluding current num
            nums_without_curr = nums[:i] + nums[i+1:]
            # Here we recursively find every permutation of nums_without_curr
            # And append curr to the front of all these smaller permutations
            # Store this in our current perms (which gets bigger by 1 element with
            # each level we recurse back up
            # So for each iteration of the outer loop, we cover all permutations
            # where the ith element is at the front, so if i takes on every value
            # in nums, we are guaranteed to create every permuation
            for p in self.permute(nums_without_curr):
                perms.append([curr] + p)

        return perms
        # Returns the permuations of smaller subproblems to bigger ones so that they
        # may fill their perms by appending the next higher level's curr to the front
        # of each list contained in the lower recursive level's perms.
        # When we reach the top-level recursion, perms will have size (len(nums))!
        # and will have every permutation of a list of len(nums) which finally gets
        # returned as the Solution
