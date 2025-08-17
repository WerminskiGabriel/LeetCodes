class Solution:
    def longestPalindrome(self, s: str) -> str:
       
        def odd( i , left , right ) :
        #	left = right = i
            res = 0
            s_res = []
            while left >= 0 and right < len( s ) :
                if s[left] == s[right] :
                    leng = right - left + 1
                    if leng > res :
                        s_res.append( s[right] )
                        res = leng
                else :
                    break
                left -= 1
                right += 1
            return s_res

        max_even = max_odd = []
        for i in range( len( s ) ) :

            new = odd( i,i,i )
            if len( max_odd ) < len( new ) :
                max_odd = new

            new = odd( i, i, i+1 )
            if len( max_even ) < len( new ) :
                max_even = new

        max_even = "".join(  max_even[::-1] ) + "".join( max_even )
        max_odd = "".join(max_odd[len(max_odd)-1:0:-1])  +max_odd[0] +"".join(max_odd[1:])
        if len( max_odd ) > len( max_even ) :
            return max_odd
        return max_even 