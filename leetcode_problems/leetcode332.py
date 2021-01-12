"""
Find a valid itinerary from the tickets, in lexographical order if multiple poss
Uses DFS: follows possible path until reaches end point (only one possible)
These will all be accessed in lexographical order, and added to the itinerary
  in reverse order (postvisit)
Essentially there is a main line from the start to end points.
    Depending on lexography, some auxilliary cycles get dealt with on the way
    The remaining cycles are dealt with on the way back to the beginning
Itinerary is then reversed.

Destinations is an adjacency dictionary, with adjacent nodes stored in lex order
"""



from collections import deque

def findItinerary(tickets):
    tickets.sort(key=lambda x:x[1])
    destinations = {}
    for ticket in tickets:
        if ticket[0] in destinations:
            destinations[ticket[0]].append(ticket[1])
        else:
            destinations[ticket[0]] = deque([ticket[1]])

    itinerary = []
    def DFS(v):
        if v in destinations:
            while destinations[v]:
                DFS(destinations[v].popleft())
        itinerary.append(v)

    DFS('JFK')
    return itinerary[::-1]

tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]

print(findItinerary(tickets))
