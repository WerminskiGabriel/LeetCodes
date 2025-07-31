class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        def quick_sort( T ) :
            def partition( T , left , right ) :
                mid = ( left + right ) // 2 
                pivot = T[mid][0]
                i = left
                j = right

                while True :
                    while T[i][0] < pivot :
                        i += 1
                    while T[j][0] > pivot :
                        j -= 1 
                    if i >= j : 
                        return j 
                    T[i] , T[j] = T[j] , T[i]
                    i += 1
                    j -= 1
            
            def in_quick( T , left , right ) :
                if left < right : 
                    q = partition( T , left , right )
                    in_quick( T , left , q ) 
                    in_quick( T , q+1 , right )
            in_quick( T , 0 , len( T )-1 ) 
        
        def insertion_sort( t ) :
            for i in range( 1, len( t ) ) :
                for j in range( i-1, -1, -1 ) :
                    if t[j][0] > t[j+1][0] :
                        t[j],t[j+1]=t[j+1],t[j]
                    else:
                        break
        
        temp = []
        for i in range( len( nums ) ) :
            temp.append( (nums[i] , i) )
        nums = temp
        n = len( nums )-1
        if n < 10 :
            insertion_sort( nums ) 
        else :
            quick_sort( nums )
        
        i = 0 
        j = n
        
        while i <= j  :
            sum = nums[i][0] + nums[j][0] 
            if sum == target :
                return nums[i][1] , nums[j][1]
            elif sum < target : 
                i += 1
            elif sum > target : 
                j -= 1
#end
