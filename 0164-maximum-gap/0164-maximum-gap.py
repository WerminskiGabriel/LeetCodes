class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()

        n = len( nums )
        if n <= 1  :
            return 0

        res = abs( nums[0] - nums[1] )
        for i in range( 2, n ) :
            res = max( res , abs( nums[i-1] - nums[i] ) )

        return res 