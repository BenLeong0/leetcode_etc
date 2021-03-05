def solution(banana_list):
    def gcd(x, y):
       while(y):
           x, y = y, x % y
       return x

    def can_pair(a,b):
        while True:
            if a == b:
                return False

            g = gcd(a,b)
            while g != 1:
                a //= g
                b //= g
                g = gcd(a,b)

            if (a + b) % 2 == 1:
                return True
            a, b = max(a,b), min(a,b)
            a, b = a-b, 2*b
        return True

    # Find maximum matching
    n = len(banana_list)
    # matching = set()
    # covered = set()
    adj = [set() for _ in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            if can_pair(banana_list[i],banana_list[j]):
                adj[i].add(j)
                adj[j].add(i)

    def dfs(u, matching, visited):
        for v in range(n):
            if v in adj[u] and not visited[v]:
                visited[v] = True
                if matching[v] == -1 or dfs(matching[v], matching, visited):
                    matching[v] = u
                    return True
        return False


    matching = [-1] * n
    number_of_pairs = 0
    for u in range(n):
        visited = [False] * n
        if dfs(u,matching,visited):
            number_of_pairs += 1

    return n - 2*(number_of_pairs//2)

    # def dfs(node, path):
    #     # check each adj node not in path
    #     # if not covered, done!
    #     # if covered, add to path and continue from other end of matched edge
    #     for adj_node in adj[node]:
    #         if visited[adj_node]:
    #             continue
    #
    #         elif adj_node not in covered:
    #             for i in range(1,len(path),2):
    #                 matching.remove(tuple(sorted(path[i:i+2])))
    #             path.append(adj_node)
    #             for i in range(0,len(path),2):
    #                 matching.add(tuple(sorted(path[i:i+2])))
    #             covered.update((path[0], path[-1]))
    #             return True
    #
    #         else:
    #             for edge in matching:
    #                 if adj_node not in edge:
    #                     continue
    #                 other_node = edge[0] if (adj_node == edge[1]) else edge[1]
    #                 visited[adj_node] = True
    #                 visited[other_node] = True
    #                 if dfs(adj_node, path+[adj_node,other_node]):
    #                     return True
    #                 visited[adj_node] = False
    #                 visited[other_node] = False
    #                 break
    #     return False
    #
    # for i in range(n):
    #     if i not in covered:
    #         visited = [False] * n
    #         visited[i] = True
    #         dfs(i,[i])
    #
    # return n-len(covered)


banana_list=[1,2]
# banana_list=[1, 2, 1, 7, 3, 21, 13, 19]
# banana_list = [1, 7, 3, 21, 13, 19]
print(solution(banana_list))
