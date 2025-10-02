class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
            
            
        numEmpty = 0
        result = 0

        while numBottles > 0 :

            result += numBottles
            numEmpty += numBottles
            numBottles = 0

            while numEmpty >= numExchange :
                numEmpty -= numExchange
                numBottles += 1
                numExchange += 1

        return result