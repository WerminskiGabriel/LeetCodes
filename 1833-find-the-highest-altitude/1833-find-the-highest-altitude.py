class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current = 0
        max_c = 0

        for i in range( len( gain ) ) :
            current += gain[i]
            max_c = max( current , max_c ) 

        return max_c
        