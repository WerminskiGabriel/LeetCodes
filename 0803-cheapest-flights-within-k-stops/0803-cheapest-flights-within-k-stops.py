class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:   
        import queue
       	A = [ [] for i in range( n )  ]
        for u , v , cost in flights :
            A[u].append( ( v , cost )  )

        inf = float( "inf" )

        d = [ [ inf for i in range( k+2 ) ] for i in range( n ) ]
        d[src][0] = 0

        def BFS( src , dst , k ) :
            q = queue.PriorityQueue()
            q.put( [ 0  , src , 0 ] )

            while not q.empty() :
                dist , u , time = q.get()

                if time > k or dist > d[u][time] :
                    continue

                for v , cost in A[u] :

                    if dist + cost < d[v][time+1] :
                        d[v][time+1] = dist + cost
                        q.put( [ d[v][time+1] , v , time+1 ] )
            

        BFS( src, dst , k )
  
        res = min( d[dst] ) 

        return res if res != inf else -1