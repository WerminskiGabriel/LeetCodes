class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        temp = 0
        for num in nums :
            temp = temp ^ num
        return temp