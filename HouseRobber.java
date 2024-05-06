class Solution {
    public int rob(int[] nums) {
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
}
