class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        # Classic binary search algorithm
        while l <= r:
            mid = (l + r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return l # The smallest satisfactory bound for which an unfound target could be inserted
