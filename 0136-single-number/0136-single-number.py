class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from collections import Counter
        nums = Counter(nums)
        for item , val in nums.items() :
            if val == 1 :
                return item