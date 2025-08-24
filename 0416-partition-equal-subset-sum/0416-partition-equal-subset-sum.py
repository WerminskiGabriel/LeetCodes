class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums.sort()
        all_sum = sum( nums )
        memo = {}
        def rec( idx , used ) :

            key = (idx,used)
            if key in memo :
                return memo[key]

            if idx == len( nums ) :
                return False
            nonlocal all_sum

            if used == all_sum - used :
                return True

            memo[key] = rec( idx+1 , used + nums[idx] ) or rec( idx+1 , used )
            return memo[key]
        return rec( 0 , 0 )