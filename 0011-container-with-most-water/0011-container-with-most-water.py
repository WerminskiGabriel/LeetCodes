class Solution:
    def maxArea(self, height: List[int]) -> int:
        lenght = len( height )
        i , j = 0 , lenght - 1

        max_volume = 0

        while i < j :
            tall = min( height[i] , height[j] )
            wide = j - i
            max_volume = max( max_volume , tall * wide )

            if height[i] < height[j] :
                i += 1
            else :
                j -= 1

        return max_volume