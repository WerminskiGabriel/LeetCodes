class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        
        stack = []

        for idx, temp in enumerate( temperatures ) :

            sum = 0
            

            while stack and temperatures[ stack[-1] ] < temp :
                small_idx = stack.pop()
                temperatures[ small_idx ] = idx - small_idx

            stack.append( idx )
        while stack : 
            temperatures[ stack.pop() ] = 0
        return temperatures
