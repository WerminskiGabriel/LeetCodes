class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len( nums )

        i = j = 0
        max_leng = 0
        last_zero = -1

        while j < n :
            if nums[j] == 0 :
                if last_zero <= i :
                    max_leng = max( max_leng , j-i-1 )
                    i = last_zero+1
                    last_zero = j
                else :
                    max_leng = max( max_leng , j-i-1 )
                    i = last_zero + 1
                    last_zero = j
            j += 1

        return max( max_leng , j-i-1 )