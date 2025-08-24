class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        n = len( nums )
        nums = sorted( nums ,  reverse = True )

        memo = {}
        def rec( i ) :
            if i in memo :
                return memo[i]
            nonlocal n
            if i == n :
                return 0

            j = i
            res = 0

            while j < n and nums[j] == nums[i] :
                res += nums[i]
                j += 1
            res_out = rec( j )

            while j < n and nums[j] == nums[i] - 1 :
                j += 1

            #rint( res + rec( j ) , res_out )
            memo[i] = max( res + rec( j ) , res_out )
            return memo[i]

        return rec( 0 )