class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
            
        len1 , len2 = len( str1 ) , len( str2 )
        if len1 > len2 :
            str1 , str2 = str2 , str1
            len1 , len2 = len2 , len1

        res = ""
        for l in range( 1 , len1 + 1 ) :
            if len2 % l != 0 or len1 % l != 0 :
                continue
            temp = str1[:l]
            temp_multiplied_orignal = temp * ( len1 // l )
            temp_multiplied = temp * ( len2 // l )
            if temp_multiplied == str2 and temp_multiplied_orignal == str1:
                res = temp
        return res