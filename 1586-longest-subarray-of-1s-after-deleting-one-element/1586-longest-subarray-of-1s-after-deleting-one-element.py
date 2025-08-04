class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len( nums )

        left = [0] * n
        right = [0] * n

        A = [0 , n-1]

        for i in range( 1 , n ) :
            if nums[i-1] == 0 :
                A.append( i-1 )
                left[i] = 0
            else :
                left[i] = left[i-1] + 1
        for i in range( n-2 , -1, -1 ) :
            if nums[i+1] == 0 :
                right[i] = 0
            else :
                right[i] = right[i+1] + 1
        max_cnt = 0
        for idx in A :
            max_cnt = max( max_cnt , left[idx] + right[idx] )

        return max_cnt