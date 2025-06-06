class Solution {
    public int search(int[] nums, int target) {
        if (nums == null || nums.length == 0) {
            return -1;
        }

        int piv = findPivot(nums);

        // Try searching in first half
        int res = binSearch(nums, 0, piv - 1, target);
        if (res != -1) return res;

        // Try searching in second half
        return binSearch(nums, piv, nums.length - 1, target);
    }

    public int findPivot(int[] arr) {
        int l = 0;
        int r = arr.length - 1;

        while (l < r) {
            int mid = l + (r - l) / 2;
            if (arr[mid] > arr[r]) {
                l = mid + 1;
            } else {
                r = mid;
            }
        }
        return l;
    }

    public int binSearch(int[] arr, int left, int right, int target) {
        int l = left;
        int r = right;

        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (arr[mid] == target) return mid;
            else if (arr[mid] > target) r = mid - 1;
            else l = mid + 1;
        }

        return -1;
    }
}
