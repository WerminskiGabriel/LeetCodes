class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len( nums )
        cnt = [0] * 3

        for i in range( n ) :
            cnt[ nums[i] ] += 1
        idx = 0
        for i in range( n ) :
            while cnt[idx] == 0 :
                idx += 1
            nums[i] = idx
            cnt[idx] -= 1
            