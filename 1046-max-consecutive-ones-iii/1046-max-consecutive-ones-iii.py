class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        length = len( nums )
        i = 0
        max_value = 0
        current_value = 0

        if k == 0 :
            while i < length :
                if nums[i] == 1 :
                    current_value += 1
                else :
                    max_value = max( max_value , current_value )
                    current_value = 0
                i += 1
        else :
            from collections import deque
            start = 0
            que = deque( )
            while i < length and nums[i] == 0 :
                if k > len( que ) :
                    current_value += 1
                    que.append( i )
                elif k <= len( que ) :
                    last_i = que.popleft( )
                    start = que[0] if que else last_i + 1
                    que.append( i )

                i += 1

            while i < length :
                if nums[i] == 0 :
                    if len( que ) < k :
                        que.append( i )
                        current_value += 1
                    else :
                        max_value = max( max_value , current_value )
                        if nums[que[0] - 1] == 1 :
                            current_value -= (que[0] - start)
                            start = que.popleft() + 1
                            que.append( i )
                        else :
                            start = que.popleft( ) + 1
                            que.append( i )
                else :
                    current_value += 1
                i += 1

        return max( current_value , max_value )