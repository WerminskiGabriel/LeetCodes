class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
          
      n = len( rooms )
      visited = [ False ] * n
      cnt = 0
      
      def dfs( u ) :
        visited[u] = True
        nonlocal cnt
        cnt += 1
        for v in rooms[u] :
          if not visited[v] :
            dfs( v )

      dfs( 0 )

      return cnt == n
            