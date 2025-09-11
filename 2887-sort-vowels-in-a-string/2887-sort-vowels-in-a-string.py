class Solution:
    def sortVowels(self, s: str) -> str:
        
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        found_vowels = sorted( [ char for char in s if char in vowels ] , reverse = True )

        result = [ ]

        for char in s  :
            if char in vowels:
                result.append( found_vowels.pop() )
            else :
                result.append( char )

        return "".join(result)