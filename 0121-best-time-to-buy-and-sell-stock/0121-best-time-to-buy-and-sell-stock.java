class Solution {
    public int maxProfit(int[] prices) {
    
        int min_val = Integer.MAX_VALUE;
        int res = 0 ;

        for( int i = 0 ; i < prices.length ; i ++ ) { 
            min_val = Math.min( min_val, prices[i] );
            res = Math.max( res , prices[i] - min_val );
        }

        return res;
    }
}