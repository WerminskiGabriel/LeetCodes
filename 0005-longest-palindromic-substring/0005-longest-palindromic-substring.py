class Solution:
    def longestPalindrome(self, s: str) -> str:
       	def odd( i , left , right ) :
            res = 0
            while left >= 0 and right < len( s ) :
                if s[left] == s[right] :
                    leng = right - left + 1
                    if leng > res :
                        res = leng
                else :
                    break
                left -= 1
                right += 1
            return res

        start = 0
        end = 0
        for i in range( len( s ) ) :
            res = max( odd( i,i,i) , odd( i, i, i+1 ) )
            if end - start < res :
                start = i-(res-1)//2
                end = i+res//2
        return s[start:end+1]