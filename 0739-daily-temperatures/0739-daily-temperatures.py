class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        
        stack = []
        idx = len(temperatures)-1

        while idx >= 0 :
            curr_temp = temperatures[idx]
            sum = 0
            while stack and stack[-1][0] <= curr_temp :
                sum += stack.pop()[1]

            if stack  : 
                sum += 1 
            else :
                sum = 0

            stack.append( (curr_temp,sum))
            temperatures[idx] = sum          
            idx -= 1

        return temperatures
