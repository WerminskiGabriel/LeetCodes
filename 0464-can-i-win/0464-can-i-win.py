class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal == 0 : 
            return True 
            
        if (1 + maxChoosableInteger) * maxChoosableInteger // 2 < desiredTotal:
            return False
            
        memo = {}
        
        nums = [False] * (maxChoosableInteger + 1)

        def rec(current_total, nums):
            
            nums_tuple = tuple(nums)

            if nums_tuple in memo:
                return memo[nums_tuple]

            if current_total >= desiredTotal:
                return False

            for i in range(1, maxChoosableInteger + 1):
                if not nums[i]:
                    nums[i] = True
                    
                    if not rec(current_total + i, nums):
                        nums[i] = False
                        memo[nums_tuple] = True
                        return True
                    
                    nums[i] = False
            
            memo[nums_tuple] = False
            return False
        
        return rec(0, nums)