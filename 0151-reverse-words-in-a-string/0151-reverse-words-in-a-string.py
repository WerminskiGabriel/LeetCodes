class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split( sep = None, maxsplit = -1 )
        res = ""
        res += a[-1]

        for i in range( len( a )-2 , -1 , -1 ) :
            res += " " + a[i]

        return res

        return result
    