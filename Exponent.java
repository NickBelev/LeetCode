class Solution {
    public double myPow(double x, int n) {
        // Efficiently calculates x ^ |n|
        double res = helper(x, n);

        // If n is positive, we return x ^ |n|
        if (n >= 0) return res;
        // If n is negative, then x ^ n = 1 / (x ^ |n|)
        else return 1.0 / res;
    }

    private double helper(double x, int n) {
        // Base cases: 0^anything = 0; anything^0 = 1 (more or less)
        if (x == 0.0) return 0.0;
        if (n == 0) return 1;

        // recursively break down the exponent into half of its power, then we just square that later cuz 
        // x^n = x^n/2 + x^n/2 (n divides in 2 properly, if it's even.  If it's odd we lose 1 in the exponent (= * x)
        // So we figure out recursively which case we're dealing with when we break down n and adjust accordingly
        double res = helper(x, n / 2); // log_2(n) time complexity, better than linear

        if (n % 2 == 0) return res * res;
        else return res * res * x;
    }
}
