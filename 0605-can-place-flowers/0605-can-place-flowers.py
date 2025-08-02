class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0 
        leng = len( flowerbed )
        while i < leng -1 :
            if flowerbed[i] == 1  :
                i += 1 
                
            elif flowerbed[i+1] == 0 :
                n -= 1
                i += 1 
            i += 1 
        if flowerbed[leng-1] == 0 and i < leng: 
            n -= 1
        return n <= 0    