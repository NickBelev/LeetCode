class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Ex.
        # [n1, n2, n3, n4, n5]
        # Binary translation
        # n1: 0100 (4 - single number)
        # n2: 0001 (1)
        # n3: 0010 (2)
        # n4: 0001 (1)
        # n5: 0010 (2)

        # Consider bitwise XOR (x)
        # a) 0x0 = 0, 0x1 = 1 => (0xN = N (= Nx0))
        # b) 1x0 = 1, 1x1 = 0 => (1xN = N' (= Nx1))
        # From a) 0x0x0x...x0 = 0, so we can ignore any 0s
        # in the bit representations of our numbers, leaving the 1's, where
        # for every number that has a pair, its corresponding 1 will negate
        # the first 1 to a 0 by b).  
        
        # This goes for every column in the bitwise
        # representation of our nums.  This means that if we XOR every number
        # in nums except for the single number, all bits will have pair matches
        # and so either we have 0x0 or 1x1 (= 0) for those bit pair matches, 
        # across all bits of the number(s). 
        
        # So, each pair cancels out to 0000 and XORing this for all the 
        # resultant 0000s yields 0000.  Note this doesn't show why commutatity works
        # for the XOR operation, (axbxc = bxcxa), which is indeed a property that
        # allows this method to work
        
        # Either way, by the end we're left with s3s2s1s0 x 0000 = s3s2s1s0 (our 
        # single number). Hence, the efficient solution is to simply XOR n1, ... , ni
        # to reveal the single number.

        single = nums[0]
    
        for i in range(1, len(nums)):
            single = single ^ nums[i]

        return single
