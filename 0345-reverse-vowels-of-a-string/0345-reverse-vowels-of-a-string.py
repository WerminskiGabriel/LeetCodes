class Solution:
    def reverseVowels(self, s: str) -> str:
        from collections import deque

        q = deque()
        dict = {}

        vowels = "aeiouAEIOU"

        for i in range( len( vowels ) ) :
            dict[ vowels[i] ] = i

        n = len( s )
        s = list( s )

        for i in range( n ) :
            if s[i] in dict :
                q.append( s[i] )
                s[i] = 0
                
        for i in range( n-1 , -1 , -1 ) :
            if s[i] == 0 :
                s[i] = q.popleft()

        return  "".join( s )

        