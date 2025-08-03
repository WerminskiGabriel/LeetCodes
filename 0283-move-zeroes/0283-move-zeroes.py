class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        idx = 0

        for i in range( len( nums ) ) :
            if nums[i] != 0 :
                temp = nums[i]
                nums[i] = 0
                nums[idx] = temp
                idx += 1
            
    
        