class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = {
        'a': True, 'e': True, 'i': True, 'o': True, 'u': True,
        'A': True, 'E': True, 'I': True, 'O': True, 'U': True }

        found_vowels = []
        is_vowel = [False] * len( s )

        for i , char in enumerate( s ) :
            if char in vowels :
                found_vowels.append( char ) 
                is_vowel[i] = True

        
        found_vowels.sort(reverse=True)
        i = 0 

        result = ""
        for i in range( len( s ) ) :
            if is_vowel[i] :
                result += ( found_vowels.pop() )
            else :
                result += ( s[i] )

        return result     

