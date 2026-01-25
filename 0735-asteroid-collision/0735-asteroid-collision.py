class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        left = []
        right = []

        for asteroid in asteroids :
            if asteroid < 0 :
                broke = False
                while right :
                    if right[-1] < -asteroid :
                        right.pop()
                    elif right[-1] >= -asteroid :
                        broke = True
                        if right[-1] == -asteroid :
                            right.pop()
                        break
                if not broke :
                    left.append( asteroid )
            if asteroid >= 0 :
                right.append( asteroid )
        left.extend( right )
        return left