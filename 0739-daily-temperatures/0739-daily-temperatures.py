class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        

        answers = []
        while temperatures :
            curr_temp = temperatures.pop()
            sum = 0
            while stack and stack[-1][0] <= curr_temp :
                sum += stack.pop()[1]

            if stack  : 
                sum += 1 
            else :
                sum = 0
                
            stack.append( (curr_temp,sum))
            answers.append( sum )         

        return answers[-1::-1]
