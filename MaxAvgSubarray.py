class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        curr_sum = sum(nums[0:k])
        max_sum = curr_sum # Found starting value for sum of nums subarray of size k

        # When our right bound reaches the end, we have explored all subarrays of
        # size k
        for i in range(k, len(nums)):
            # Also note that nums[i] is always the bound just right
            # of our size k subarray, whereas nums[i - k] is the left
            # bound that is the starting index of the current size k
            # subarray. Both bounds shift right as i increments
            curr_sum += nums[i] - nums[i - k]
            # Avoid unnecessary of adding the k-2 middle elements.
            # Just exclude the left bound element and include a new right
            # bound element and see if this improves the sum

            # A max sum will always yield a max average when all sums
            # pertain to the same number of (k) elements
            max_sum = max(max_sum, curr_sum)

        return max_sum / k # Use the max sum to find the max average
