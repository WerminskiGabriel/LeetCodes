class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len( gas )
        gas = [ gas[i]-cost[i] for i in range( n ) ]

        if sum( gas ) < 0 : 
                    return -1

        start = 0
        total = 0
        for i in range( n ) :
            total += gas[i] 
            if total < 0 :
                total = 0 
                start = i+1
        return start
    