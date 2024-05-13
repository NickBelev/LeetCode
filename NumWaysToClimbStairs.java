class Solution {
    public int climbStairs(int n) {
        // An oddly simple solution to a complex problem.
        // When converting the decision tree into a memoized iterative DP solution, we notice the pattern
        // that the number of ways to walk up k stairs is equivalent to the sum of the number of ways to 
        // walk up k-1 and k-2 stairs as either we got to the kth stair by a single step or by a double step
        // along with the previous choices that led to the single or double step.
        // Realizing this, yields an algorithm identical to the calculation of Fibonacci numbers.
        int f = 1;
        int s = 1;
        int temp;
        while (n > 1)
        {
            --n;
            temp = s;
            s = f + s;
            f = temp;
        }

        return s;
    }
}
