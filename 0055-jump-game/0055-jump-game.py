class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n = len( nums ) 
        dest = n - 1 

        for i in range( n-2 , -1 , -1 ) :
            if i + nums[i] >= dest :
                dest = i 
        
        return dest == 0