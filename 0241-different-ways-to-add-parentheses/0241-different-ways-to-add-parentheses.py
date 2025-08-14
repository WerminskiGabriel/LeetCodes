class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        
        memo = {}
        operations = {
            "+" : lambda x,y : int(x)+int(y),
            "-" : lambda x,y : int(x)-int(y),
            "*" : lambda x,y : int(x)*int(y)
        }
        def rec( left , right ) :
            res = []
            for i in range( left , right+1 ) :
                op = expression[i]
                if op in operations :
                    nums1 = rec( left , i-1 )
                    nums2 = rec( i+1 , right )

                    for n1 in nums1 :
                        for n2 in nums2 :
                            res.append( operations[op]( n1,n2) )
            if res == [] :
                res.append( int(expression[left:right+1]) )
            return res
        return  rec( 0 , len( expression) -1 )

