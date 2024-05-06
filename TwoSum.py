class TwoSum:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to store visited numbers and their indices
        visited = {}
        # Iterate through the list with indices
        for i, num in enumerate(nums):
            # If the complement of the current number (target - num) is found in the visited dictionary,
            # return the indices of both numbers that sum up to the target
            if target - num in visited:
                return (visited[target - num], i)
            # Add the current number to the visited dictionary with its index, so that if its
            # complement appears later, it can be found in the prior if-statement
            if num not in visited:
                visited[num] = i
