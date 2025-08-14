class Solution:
    def integerReplacement(self, n: int) -> int:
        from collections import deque
        q = deque()
        q.append( ( n , -1 ) )

        while q :
            x , cnt = q.popleft()
            cnt += 1
            if x == 1 :
                return cnt

            if x%2 == 0 :
                q.append( (x//2 , cnt ) )
            else :
                q.append( (x+1 , cnt ) )
                q.append( (x-1 , cnt ) )