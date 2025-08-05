class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
       
        n = len( baskets )
        cnt = 0
    
        for i in range( n ) :
            for j in range( 0 , n ) :
                if baskets[j] >= fruits[i] :
                    baskets[j] = 0
                    cnt+=1
                    break

        return n - cnt
    