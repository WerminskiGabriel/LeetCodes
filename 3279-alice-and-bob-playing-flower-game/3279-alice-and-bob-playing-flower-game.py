class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        return n* m // 2 
        """
        cnt = 0
        mn = max( m , n ) 
        isEven = [False] * ( mn+1 ) 
        
        for j in range( 1 , mn+1 ) :
            isEven[j] = j % 2 == 0
        
        for i in range( 1 , n+1 ) :
            for j in range( 1 , m+1 ) :
                if isEven[i] :
                    if not isEven[j] : #j % 2 != 0 :
                        cnt += 1
                elif isEven[j] : #j % 2 == 0 :
                    cnt += 1

        return cnt
        """