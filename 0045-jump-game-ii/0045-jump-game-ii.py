class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len( nums )
        if n == 1 :
            return 0
        cnt = 0
        m = 0
        end = 0
        for i in range( n-1 ) :
            m = max( m ,  i + nums[i] )
            if i == end :
                cnt += 1
                end = m
        return cnt