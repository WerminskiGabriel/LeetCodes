class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len( gas )
        gas = [ gas[i]-cost[i] for i in range( n ) ]

        start = 0
        total = 0
        i = 0
        looped = False
        while i <= n :
            if i == n  :
                if looped :
                    break
                i = 0
                looped = True
            if total < 0 :
                if looped :
                    break
                start = i
                total = gas[i]
            else :
                total += gas[i]
            i += 1
            if i == start :
                break
        return start if total >= 0 else -1