class Solution:
    def isValid(self, s: str) -> bool:
            
        Stack = []

        dict = { "(":")" , "{":"}" , "[":"]" }

        for char in s :
            if not char in dict :
                if Stack and Stack[-1] == char :
                    Stack.pop()
                else :
                    return False
            else :
                Stack.append( dict[char] )

        return False if Stack else True 