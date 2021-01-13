"""
Graph searching algorithms
Both run in O(|V| + |E|), where V and E are the vertex and edge sets of the Graph
DFS is first-in-last-out  (FILO) => uses a stack
BFS is first-in-first-out (FIFO) => uses a priority queue
"""




from collections import deque
def BFS(G,s):
    queue = deque([s])
    visited = {s}
    while queue:
        v = queue.popleft()
        previsit(v)
        for (v,w) in E(G):
            if w not in visited:
                visited.add(w)
                queue.append(w)
        postvisit(v)


# No risk of stack overflow/exceeding recursion depth (if limited space)
def DFS_Iterative(G,s):
    stack = [s]
    visited = {s}
    while stack:
        v = stack.pop()
        previsit(v)
        for (v,w) in E(G):
            if w not in visited:
                visited.add(w)
                queue.append(w)


# Probably simpler, but may cause stack overflow if input too big (>10000)
# postvisit!!
def DFS_Recursive(G,s):
    visited = set()
    def DFSExplore(v,G=G):
        visited.add(v)
        previsit(v)
        for (v,w) in E(G):
            if w not in visited:
                DFSExplore(w)
        postvisit(v)
    DFSExplore(s)


def topologicalSort(G,u):
    visited = set()
    tsort = []
    def DFS(v):
        visited.add(v)
        for (v,w) in E(G):          # The condition for the ranking!!
            if w not in visited:
                DFS(w)
        tsort.append(v)
    DFS(u)
    return tsort
