class Solution:
    def compress(self, chars: List[str]) -> int :
        n = len( chars )

        count = 0
        res = []
        current = chars[0]

        idx = 0

        for char in chars :
            if char != current :
                chars[idx] = current
                idx += 1
                if count > 1 :
                    for num in str( count ) :
                        chars[idx] = num
                        idx += 1
                count = 1
                current = char

            else :
                count += 1
        chars[idx] = current
        idx += 1
        if count > 1 :
            for num in str( count ) :
                chars[idx] = num
                idx += 1
        
        return idx

