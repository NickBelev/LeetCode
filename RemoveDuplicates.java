class Solution {
    public int removeDuplicates(int[] nums) {
        // All duplicates are consecutive!

        int j = 0; // index for inserting non-duplicates once confirmed

        // iterate over nums but skip the last element
        for (int i = 0; i < nums.length - 1; i++) {
            // if the next element is different than the current,
            if (!(nums[i + 1] == nums[i])) {
            // insert the current element into the next correct spot
            // (reuse nums for space efficiency and just overwrite the previous)
            // value which would have been a duplicate
                nums[j] = nums[i];
                j++; // increment the non-duplicate insertion index
            }
        }
        nums[j] = nums[nums.length - 1];
        // for index bounds the last index is never included and always must be
        // either there were no duplicates of that value before
        // or there were duplicates which were ignored and never inserted
        
        return j + 1; // The number of unique elements (1-index counted)
    }
}
