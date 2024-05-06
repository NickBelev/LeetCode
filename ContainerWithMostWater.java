class Solution {
    public int maxArea(int[] heights) {
        // Initialize maximum area
        int max = 0;
        // Initialize current area
        int curr;
        // Initialize left pointer
        int l = 0;
        // Initialize right pointer
        int r = heights.length - 1;
        // Loop until left pointer is equal to right pointer; we've checked all possibilities using our Greedy Choice
        while (l != r) {
            // Calculate the current area by multiplying the width (distance between pointers) 
            // by the minimum height between the two vertical lines
            curr = (r - l) * Math.min(heights[l], heights[r]);
            // Update maximum area if current area is greater
            if (curr > max) max = curr;

            // Greedy Choice:
            // Move the pointer with the lesser height towards the center,
            // as keeping the pointer with greater height may result in a greater area
            if (heights[l] < heights[r]) ++l;
            else --r;
        }
        // Return the maximum area found
        return max;
    }
}
