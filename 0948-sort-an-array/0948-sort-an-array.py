class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return sorted( nums ) 
        """
        n = len( nums )
        A = [] * n

        def merge( left , mid , right ) :
            A[left : right+1] = nums[ left : right + 1 ]

            i = k = left
            j = mid + 1

            while i <= mid and j <= right :
                if A[i] < A[j] :
                    nums[k ] = A[i ]
                    i += 1
                    k += 1
                else :
                    nums[k ] = A[j ]
                    j += 1
                    k += 1
            while i <= mid :
                nums[k ] = A[i ]
                i += 1
                k += 1
            while j <= right :
                nums[k ] = A[j ]
                j += 1
                k += 1

        def in_sort( left , right ) :
            if left != right :
                mid = (left + right) // 2
                in_sort( left , mid )
                in_sort( mid+1 , right )
                merge( left , mid , right )

        in_sort( 0 , n-1 )
        return nums
"""