class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        j = len( nums ) - 1
        counter = 0

        while i < j :
            sum = nums[i] + nums[j]
            if sum == k :
                i += 1
                j -= 1
                counter += 1
            elif sum > k :
                j -= 1
            else :
                i += 1
        return  counter
