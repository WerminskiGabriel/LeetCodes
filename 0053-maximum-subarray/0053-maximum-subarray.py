class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        n = len( nums )
        i = 0
        max_sum = nums[0]

        while i < n - 1 and nums[ i ] <= 0 :
                    max_sum = max( max_sum, nums[i] )
                    i += 1
        sum = nums[i]
        i += 1

        while i < n :
            
            if 0 < sum + nums[i] :
                if nums[i] < 0 :
                    max_sum = max( max_sum ,sum )
                sum += nums[i]
    
            else :
                while i < n-1 and nums[i] <= 0 :
                    max_sum = max(max_sum , nums[i] )
                    i += 1
                max_sum = max( max_sum , sum )
                sum = nums[i]
                
            i += 1

        return max( max_sum , sum )