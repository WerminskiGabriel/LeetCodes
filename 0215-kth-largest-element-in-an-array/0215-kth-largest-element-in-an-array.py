class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k -=1 
        def hoare( left , mid , right ) :
            pivot = nums[mid]

            while True :
                while nums[left] < pivot :
                    left += 1
                while nums[right] > pivot :
                    right -= 1
                if left >= right :
                    return right
                nums[left] , nums[right] = nums[right] , nums[left]
                left += 1
                right -=1

        def quick_select( left , right ) :
            if left == right :
                return nums[left]
            if left < right :
                q = hoare( left ,(left+right) // 2, right )
                if q < k :
                    return quick_select( q+1 , right )
                else :
                    return quick_select( left , q )
        nums = [ nums[i]*-1 for i in range( len( nums ) ) ]
        return - quick_select( 0 , len( nums )-1 )