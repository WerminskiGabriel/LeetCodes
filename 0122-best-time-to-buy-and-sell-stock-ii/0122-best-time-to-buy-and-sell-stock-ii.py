class Solution:
    def maxProfit(self, prices: List[int]) -> int:
            
        n = len( prices )

        current = prices[0]
        res = 0
        
        for price in prices :
            if current >= price :
                current = price
            else :
                res += price - current
                current = price
        return res