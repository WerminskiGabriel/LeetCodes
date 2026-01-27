class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        sorted_spells = sorted( [ ( spell , idx ) for  idx , spell in enumerate( spells ) ] , key = lambda x : x[0] )
        potions.sort()

        size_potions = len( potions )
        right_idx = size_potions - 1
        result = []
        for i in range( len( spells ) ) :
            spell = sorted_spells[i][0]
            lt = success / spell
            while( right_idx >= 0 and potions[right_idx] >= lt  ) :
                right_idx -= 1
            result.append( ( sorted_spells[i][1] , size_potions - right_idx -1 ))

        return [ res for idx , res in sorted( result , key = lambda x : x[0] ) ]