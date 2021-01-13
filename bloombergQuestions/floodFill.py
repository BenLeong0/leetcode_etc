board = [
    [0,0,1,2],
    [0,1,2,1],
    [2,1,1,1]
]


def sizeOfLargestComponent(board):
    visited = {(i,j):False for i in range(len(board)) for j in range(len(board[0]))}
    maxSize = 0

    def getNeighbours(i,j):
        neighbours = []
        if i > 0:
            neighbours.append((i-1,j))
        if i < len(board)-1:
            neighbours.append((i+1,j))
        if j > 0:
            neighbours.append((i,j-1))
        if j < len(board[0])-1:
            neighbours.append((i,j+1))
        return neighbours


    for i in range(len(board)):
        for j in range(len(board[0])):
            # Only check tiles of even parity
            if (i+j)%2 == 1:
                continue
            # No need to check tiles more than once
            if visited[(i,j)]:
                continue

            colour = board[i][j]        # Save component identifier
            stack = [(i,j)]             # Initalise stack
            currSize = 0                # Memoize component's size
            while stack:
                curr = stack.pop()
                currSize += 1
                visited[curr] = True
                for neighbour in getNeighbours(*curr):
                    if board[neighbour[0]][neighbour[1]] == colour and not visited[neighbour]:
                        stack.append(neighbour)
            maxSize = max(maxSize, currSize)

    return maxSize


print(sizeOfLargestComponent(board))


"""
DFS runs in O(|V|+|E|) = O(|V|+2|V|) = O(3|V|) = O(|V|) = O(m*n)
Checks |V|/2 vertices => runs in O(|V|^2)

Space complexity O(|V|) for visited hashtable, +colours+sizes etc (constant space)
"""
