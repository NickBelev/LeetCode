class Solution {
    public int rob(int[] nums) {
        // Initialize variables to keep track of the maximum amount of money that can be robbed
        // This is how we'll do "Memoisation"
        int L = 0; // L represents the maximum amount of money that can be robbed from the left house, which is right of the ith house
        int R = 0; // R represents the maximum amount of money that can be robbed from houses on the right, which is right of the left house
        int temp; // To store intermediate calculations

        // Iterate through the houses starting from the end
        // Houses in order look like a, b, c, ... i, L, R
        // With L and R initialized to 0, since at the start, 'i' is the last house on the right
        for (int i = nums.length - 1; i >= 0; i--) {
            // Calculate the maximum amount of money that can be robbed from houses at position 'i'.
            // If we rob the house at position 'i', we add the money from this house to the money robbed from houses on the right, R
            // since we cannot rob the adjacent house to 'i', which is L, if we choose to rob 'i'.
            // Otherwise, we skip robbing 'i', and the maximum amount carries over from the left house, L.
            temp = Math.max(R + nums[i], L); // Calculate the optimal robbery: (i*, L, R*) vs (i, L*, R)
            R = L; // Then we set the new optimal value for R to be the old one for L
            L = temp; // And we set L to be the better of the choices between robbing 'i' and the previous optimal value R, or using the old L.
            // We carry on forward in the array, continuing to make the optimal choice each time.
        }
        // Return the maximum amount of money that can be robbed from all the houses which will be calculated when 'i' = 0, and stored in L.
        return L;
    }
}
