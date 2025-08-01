class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len( word1 )
        len2 = len( word2 ) 

        n = min( len1 , len2 )

        merged = ""
        for i in range( n ) :
            merged += word1[i]+word2[i]
        
        if n < len1 : 
            merged += word1[n:]
        else :
            merged += word2[n:]
        
        return merged