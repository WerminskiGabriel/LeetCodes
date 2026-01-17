class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        from collections import defaultdict

        memo = defaultdict( int )
        memo2 = set()
        for num in arr :
            memo[num] += 1
        for item in memo.values() :
            if item in memo2 :
                return False
            else :
                memo2.add( item )
        return True