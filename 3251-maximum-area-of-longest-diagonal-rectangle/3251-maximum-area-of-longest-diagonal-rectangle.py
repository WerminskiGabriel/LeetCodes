class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
            
        res = 0
        max_val = 0
        
        for x, y in dimensions :

            q = x * x + y * y
            p = x * y

            if max_val <= q :
                if max_val == q and p < res :
                    continue
                max_val = q
                res = x * y

        return res