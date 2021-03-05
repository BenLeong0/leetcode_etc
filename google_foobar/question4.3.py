from collections import deque

def solution(entrances, exits, path):
    # Networks: max flow problem!
    n = len(path)
    for i in range(n):
        path[i].append(0)
        if i in exits:
            path[i].append(2000001)
        else:
            path[i].append(0)
    path.append([2000001]*len(entrances) + [0]*(n-len(entrances)+2))
    path.append([0]*(n+2))
    s, t = n, n+1

    def bfs_exists_path(N):
        visited = [False] * (n+2)

        Q = deque([s])
        visited[s] = True
        paths = {s: []}

        while Q:
            u = Q.popleft()
            for v in range(n+2):
                if N[u][v] > 0:
                    if v == t:
                        return paths[u] + [(u,t)]
                    if not visited[v]:
                        visited[v] = True
                        paths[v] = paths[u] + [(u,v)]
                        Q.append(v)
        return []

    def min_cap(N, route):
        cap = 2000001
        for (u,v) in route:
            cap = min(cap, N[u][v])
        return cap

    def val(f):
        value = 0
        for (u,v) in f:
            if u == s:
                value += f[(u,v)]
            elif v == s:
                value -= f[(u,v)]
        return value

    def residual_network(f):
        N = [[0]*(n+2) for _ in range(n+2)]
        for u in range(n+2):
            for v in range(n+2):
                if path[u][v] > 0:
                    if f[(u,v)] < path[u][v]:
                        N[u][v] = path[u][v] - f[(u,v)]
                    if f[(u,v)] > 0:
                        N[v][u] = f[(u,v)]
        return N

    def ford_fulkerson():
        f = {}
        for u in range(n+2):
            for v in range(n+2):
                if path[u][v] > 0:
                    f[(u,v)] = 0
                    f[(v,u)] = 0
        N = residual_network(f)
        route = bfs_exists_path(N)
        while route:
            aug_val = min_cap(N, route)
            for (u,v) in route:
                f[(u,v)] += aug_val
            N = residual_network(f)
            route = bfs_exists_path(N)
        return val(f)

    return ford_fulkerson()


    for row in path:
        print(row)

print(solution([0], [3], [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]))
