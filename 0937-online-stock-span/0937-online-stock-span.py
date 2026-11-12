class StockSpanner:

    def __init__(self):
        self.values = []
        self.spans = []

    def next(self, price: int) -> int:    

        span = 1
        while self.values and price >= self.values[-1] :
            self.values.pop()
            span +=  self.spans.pop()
        
        self.values.append( price )
        self.spans.append(span)
        return span
        



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)