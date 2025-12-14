class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        memo1 = set( nums1 )
        memo2 = set( nums2 )

        res = [ [] for _ in range( 2 ) ]
        
        for num in memo1 :
            if num not in memo2 :
                res[0].append( num )
            else :
                memo2.remove( num )
        
        res[1].extend( list(memo2) )

        return res 
