class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        alloted = 0
        for i in range(n):
            for j in range(n):
                if fruits[i] <= baskets[j]:
                    baskets[j] = -1  # mark as used
                    alloted += 1
                    break
        return n - alloted
        
        n = len( baskets )
        cnt = 0
        """
        for i in range( n ) :
            for j in range( 0 , n ) :
                if baskets[j] and baskets[j] >= fruits[i] :
                    baskets[j] = 0
                    break
                if j == n-1 :
                    cnt += 1

        return cnt
        """