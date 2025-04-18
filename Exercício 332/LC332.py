class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        graph = defaultdict(list)
        
        for departure, arrival in sorted(tickets, reverse=True):
            graph[departure].append(arrival)

        itinerary = []
        
        def dfs(airport):
            while graph[airport]:
                next_airport = graph[airport].pop()
                dfs(next_airport)

            itinerary.append(airport) 
        
        dfs("JFK")
        
        return itinerary[::-1]
