class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        n = len( nums )
        
        if k-1 >= n :
            return 0

        i = 1 
        j = k
        
        sums = sum( nums[:k] )
        max_sum = sums

        while j < n :
            sums = sums - nums[i-1] + nums[j]
            max_sum = max( max_sum , sums )
            i += 1 
            j += 1
        return max_sum / k