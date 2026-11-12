class StockSpanner:

    def __init__(self):
        self.values = []

    def next(self, price: int) -> int:    

        span = 1
        while self.values and price >= self.values[-1][0] :
            span +=  self.values.pop()[1]
        
        self.values.append( (price,span) )
        return span
        



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)