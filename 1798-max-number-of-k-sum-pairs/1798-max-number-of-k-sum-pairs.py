class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        dict = {}
        for num in nums :
            if num in dict :
                dict[num] += 1
            else :
                dict[num] = 1
        res = 0
        for num , num_cnt in dict.items():
            looked = k - num
            if looked < num or looked not in dict : continue
            if num != looked :
                res += ( min( num_cnt , dict[looked] ) )
            else :
                res += num_cnt // 2
        return res