class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        from queue import PriorityQueue

        def dijsktra( x ) :
            a , b = x[0] , x[1]
            
            if not (a in dict and b in dict) :
                return -1.0

            start = dict[a]
            end = dict[b]

            if start in dict :
                return d[end] if d[end] != inf else -1

            if start == end :
                return 1.0
            n = len( adj_list )

            d = d_empty.copy()
            d[start] = 1

            pq = PriorityQueue()
            pq.put( ( 0 , start ) )

            while not pq.empty() :
                dist , u = pq.get()
                for v , val in adj_list[u] :
                    if d[v] > d[u] * val :
                        d[v] = d[u] * val
                        pq.put(  (d[v] , v) )
            d_results[ start ] = d
            return d[end] if d[end] != inf else -1


        n = 2 *len( equations )
        dict = {}
        adj_list = [ [] for i in range( n ) ]

        i = 0
        j = 0
        for l in equations :
            a , b = l[0] , l[1]
            if not a in dict :
                dict[a] = i
                i += 1
            if not b in dict :
                dict[b] = i
                i += 1
            adj_list[ dict[a] ].append( (dict[b] , values[ j ] ) )
            adj_list[ dict[b] ].append( (dict[a] , 1 / values[ j ]))
            j += 1

        for j in range( n - i ) :
            adj_list.pop()
            
        d_results = {}
        inf = float( "inf" )
        res = []
        d_empty = [ inf for _ in range( i ) ]

        for x in queries :
            res.append( dijsktra( x ) )

        return res