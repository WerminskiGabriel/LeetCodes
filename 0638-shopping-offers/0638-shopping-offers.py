class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        memo = {}

        def rec( needs ) :
            tuple_needs = tuple( needs )

            if tuple_needs in memo :
                return memo[tuple_needs]

            needs_len = len( needs )
            res = 0

            for i in range( needs_len ) :
                res += needs[i] * price[i]

            for i in range( len( special ) ) :
                is_valid = True
                new_needs = list( tuple_needs )

                for j in range( needs_len ) :
                    if new_needs[j] < special[i][j] :
                        is_valid = False
                        break
                    new_needs[j] -= special[i][j]

                if is_valid :
                    res = min( res , special[i][ needs_len ] + rec( new_needs ) )

            memo[tuple_needs ] = res
            return res
        return rec( needs )