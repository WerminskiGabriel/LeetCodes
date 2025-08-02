class Solution:
    def reverseWords(self, s: str) -> str:
        from collections import deque

        q = deque()
        current = ""
        n = len ( s )

        for i in range( n ) :
            if current != "" and s[i] == " ":
                q.append( current )
                current = ""

            if s[i] != " " :
                current += s[i]
        if current != "" :
            q.append( current )

        result =  ""
        if q :
            result += q.pop()
        while q :
            result += " " + q.pop()

        return result
    