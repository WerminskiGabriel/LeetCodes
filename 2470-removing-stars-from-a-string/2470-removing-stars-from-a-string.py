class Solution:
    def removeStars(self, s: str) -> str:
        Stack = []
        for char in s  :
            if char == "*" :
                Stack.pop()
            else :
                Stack.append( char )
        return "".join( Stack )
        