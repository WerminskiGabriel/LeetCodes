class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        memo = {}

        for num in nums :
            if num in memo :
                return True
            else :
                memo[num] = 0
        return False 