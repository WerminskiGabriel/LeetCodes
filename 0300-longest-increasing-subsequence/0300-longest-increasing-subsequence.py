class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
                def binfun( i ) :

                    left = 0
                    right = len( res ) -1

                    x = nums[i]

                    while left <= right :

                        if left == right :
                            return left

                        mid = ( left + right ) // 2

                        if res[mid] == x :
                            return mid
                        elif res[mid] < x :
                            left = mid+1
                        else :
                            right = mid

                    return right

                n = len( nums )

                res = []
                res.append( nums[0] )

                used = {nums[0] : 0}

                for i in range( 1, n ) :

                    if nums[ i ] in res :
                    	continue
                    if nums[i] > res[-1] :
                        res.append( nums[i] )
                    else :
                        idx = binfun( i )
                        res[ idx ] = nums[i]

                    used[ nums[i] ] = 0

                return len( res )