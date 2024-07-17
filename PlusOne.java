class Solution {
    public int[] plusOne(int[] digits) {

        for (int i = digits.length - 1; i >= 0; i--) { // Work from back to front, like grade school addition
            if (digits[i] != 9) {
                digits[i]++; // If we can successfully increment in one place we don't need to continue
                break;
            }
            digits[i] = 0; // If it was a 9, we have a carryover and continue towards the front
        }

        if (digits[0] == 0) { // this case triggers if we do 999...9 + 1 (end up with overflow)
            digits = new int[digits.length + 1]; // defaults to all 0's, with space for a 1 in the front
            digits[0] = 1; // change first digit to 1
        }
        return digits;
    }
}
