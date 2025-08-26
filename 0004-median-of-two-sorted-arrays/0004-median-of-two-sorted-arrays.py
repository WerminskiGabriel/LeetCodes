class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for num in nums2 :
            nums1.append( num )
        nums1.sort()
        return nums1[ len(nums1) // 2 ] if len(nums1 ) % 2 != 0 else ( nums1[ len(nums1) //2 -1 ] + nums1[len(nums1)//2] ) / 2

