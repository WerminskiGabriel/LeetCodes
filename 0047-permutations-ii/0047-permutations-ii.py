class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
            
        nums.sort()
        n = len( nums )
        used = [False] * n
        result = []
        res = []

        def backtrack() :

            if len( res ) == n :
                result.append( res.copy() )
                return

            for i in range( n ) :
                if used[i] :
                    continue
                if i > 0 and nums[i-1] == nums[i] and not used[i-1] :
                    continue

                used[i] = True
                res.append( nums[i] )
                backtrack()
                res.pop()
                used[i] = False

        backtrack()
        return result