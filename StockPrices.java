class Solution {
    public int maxProfit(int[] prices) {

        int lowest_buy_price = prices[0];
        int max_profit = 0;

        for (int i = 1; i < prices.length; i++) {
            // Determine and update lowest buy price as we iterate through the days
            if (prices[i] < lowest_buy_price) lowest_buy_price = prices[i];
            // If we were to sell today what would be the profit, assuming we bought 
            // at the lowest cost available prior to selling
            // and is this profit higher than the previously discovered maximum?
            // If we updated the price this iteration, profit would be 0, so no need to 
            // recalculate max profit
            else max_profit = Math.max(max_profit, prices[i] - lowest_buy_price);
        }

        return max_profit;

    }
}
