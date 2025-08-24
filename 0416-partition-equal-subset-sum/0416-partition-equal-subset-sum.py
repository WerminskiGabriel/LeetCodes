class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        target = sum( nums )
        if target % 2 != 0 :
            return False

        target //= 2

        dp = [ False ] * (target +1)
        dp[0] = True
        for num in nums : 
            if num > target :
                return False
            for i in range( target , 0 , -1 ) :
                if i - num < 0 :
                    break
                dp[i] = dp[i] or dp[ i - num ]

        return dp[target]