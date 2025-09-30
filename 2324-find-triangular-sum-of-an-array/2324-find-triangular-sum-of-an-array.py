class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        
        n = len( nums )
        for i in range( 1 , n ) :
            for j in range( n - i ) :
                nums[j] = ( nums[j] + nums[j+1] ) % 10
        
        return nums[0]