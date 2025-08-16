class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        n = len( nums )
        nums.sort()
        res =[]

        for i in range( n-3 ) :
            if i > 0 and nums[i-1] == nums[i] :
                continue
            for j in range( i+1 , n-2 ) :
                if j > i+1 and nums[j-1] == nums[j] :
                    continue
                k = j+1
                l = n-1

                while k < l :
                    sum = nums[i] + nums[j] + nums[k] + nums[l]
                    if sum == target :
                        res.append( [nums[i],nums[j],nums[k],nums[l]] )
                        k += 1
                        while k < l and nums[k] == nums[k-1] :
                            k += 1
                    elif sum > target :
                        l -= 1
                    else :
                        k += 1
        return res
