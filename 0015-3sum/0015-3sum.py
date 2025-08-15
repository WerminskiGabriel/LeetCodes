class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len( nums )

        res = []

        for i in range( n-2 ) :
            if i > 0 and nums[i-1] == nums[i] :
                continue
            j = i+1
            k = n-1
            while j < k :
                sum  = nums[i] + nums[j] + nums[k]

                if sum == 0 :
                    res.append( [nums[i],nums[j],nums[k]] )
                    j += 1
                    while nums[j-1] == nums[j] and j < k :
                        j += 1

                elif sum > 0 :
                    k -= 1

                else :
                    j += 1

        return res