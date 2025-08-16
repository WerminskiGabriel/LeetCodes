class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        current = 0
        cnt = 0
        for num in nums :
            if cnt == 0 :
                current = num

            if num == current :
                cnt += 1
            else :
                cnt -= 1
        return current
