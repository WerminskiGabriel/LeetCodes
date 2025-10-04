class Solution:
    def maxArea(self, height: List[int]) -> int:

        n = len( height )

        i = 0
        j = n - 1

        max_volume = j * min( height[i] , height[j] )

        while i < j :

            if height[i] < height[j] :
                i += 1

            else :
                j -= 1

            max_volume = max( max_volume , ( j-i ) * min( height[i] , height[j] ) )

        return max_volume