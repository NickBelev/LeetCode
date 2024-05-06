class Solution {
    public int rob1(int[] nums) {
        int L = 0;
        int R = 0;
        int temp;

        for (int i = nums.length - 1; i >= 0; i--) {
            temp = Math.max(R + nums[i], L);
            R = L;
            L = temp;
        }
        return L;
    }
    
    public int rob(int[] nums) {
        if (nums.length == 1) return nums[0];
        if (nums.length == 0) return 0;
        int[] nums1 = new int[nums.length - 1];
        int[] nums2 = new int[nums.length - 1];
        for (int i = 0; i < nums.length - 1; i++) {
            nums1[i] = nums[i];
            nums2[i] = nums[i+1];
        }
        return Math.max(rob1(nums1), rob1(nums2));
    }
}
