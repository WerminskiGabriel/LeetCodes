class Solution:
    def maxVowels(self, s: str, k: int) -> int:
    
        n = len( s )
        counter = 0
        vowels = "aeiou"
        dict = {}
        for vowel in vowels :
            dict[ vowel ] = False

        i = 0
        while i < k and i < n :
            if s[i] in dict :
                counter += 1
            i += 1


        if i >= n or counter == k:
            return counter

        max_counter = counter
        
        i = 1
        j = k
        while j < n :
            if s[j] in dict :
                counter += 1
            if s[i-1] in dict :
                counter -= 1
            i += 1
            j += 1
            max_counter = max( counter , max_counter )

        return max_counter