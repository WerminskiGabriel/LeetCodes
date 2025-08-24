class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
            
        Counter = {}
        for num in nums :
            if num in Counter :
                Counter[num] += 1
            else :
                Counter[num] = 1

        nums = sorted( Counter.keys() )
        n = len( nums )
        nums = [ ( nums[i] , nums[i] * Counter[nums[i]] ) for i in range( n ) ]

        dp = [0] * n
        dp[0] = nums[0][1]

        for i in range( 1 , n ) :

            if nums[i-1][0] + 1 == nums[i][0] :
                dp[i] = nums[i][1]
                
                if i - 2 >= 0 :
                    dp[i] += dp[i-2]
                dp[i] = max( dp[i] , dp[i-1] )

            else :
                dp[i] = dp[i-1] + nums[i][1]

        return dp[n-1]