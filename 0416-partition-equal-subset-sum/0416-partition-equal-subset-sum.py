class Solution:
    def canPartition(self, nums: List[int]) -> bool:
            
        #nums.sort()
        target = sum( nums ) 

        memo = {}
        def rec( idx , used ) :
            key = (idx,used)
            if key in memo :
                return memo[key]
            
            nonlocal target
            if used == target :
                return True
            
            if used > target or idx == len( nums ) :
                return False

            res = rec( idx+1 , used + nums[idx] ) or rec( idx+1 , used )
            memo[key] = res
            return res

        if target % 2 == 0 :
            target //= 2
            return rec( 0 , 0 )
        else :
            return False