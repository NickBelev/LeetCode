class Solution {
    public int maxArea(int[] heights) {
        int max = 0;
        int curr;
        int l = 0;
        int r = heights.length - 1;
        while (l != r) {
            curr = (r - l) * Math.min(heights[l], heights[r]);
            if (curr > max) max = curr;

            if (heights[l] < heights[r]) ++l;
            else --r;
        }
        return max;
    }
}
