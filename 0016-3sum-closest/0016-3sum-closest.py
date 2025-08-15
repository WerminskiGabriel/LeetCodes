class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len( nums )
        res = float( "inf" )

        for i in range( n -2 ) :
            j = i+1
            k = n-1
            while j < k :
                sum = nums[i] + nums[j] + nums[k]
                if abs(res-target) > abs( sum - target ) :
                    res = sum
                if sum == target :
                    return sum

                elif sum > target :
                    k -= 1
                else :
                    j += 1
        return res


"""
        
        nums.sort()
        n = len( nums )
        res = float( "inf" )
        val = 0

        for i in range( n -2 ) :
            j = i+1
            k = n-1
            while j < k :
                sum = nums[i] + nums[j] + nums[k]
                dist = abs( sum - target )
                if res > dist :
                    res = dist
                    val = sum
                res = min( res,  dist )
                if sum == target :
                    return 0

                elif sum > 0 :
                    k -= 1
                else :
                    j += 1
        return val"""