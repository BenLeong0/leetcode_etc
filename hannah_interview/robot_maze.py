from typing import List, Tuple

maze = [
    [0, 0, 0, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 0]
]
start_point = (1,0)
end_point = (2,2)


def get_neighbours(maze, x, y):
    neighbours = []
    if x > 0 and maze[x-1][y] == 0:
        neighbours.append((x-1, y))
    if x < len(maze)-1 and maze[x+1][y] == 0:
        neighbours.append((x+1, y))
    if y > 0 and maze[x][y-1] == 0:
        neighbours.append((x, y-1))
    if y < len(maze[0])-1 and maze[x][y+1] == 0:
        neighbours.append((x, y+1))
    return neighbours


def find_shortest_route(
    maze: List[List[int]],
    start_point: Tuple[int, int],
    end_point: Tuple[int, int]
) -> List[Tuple[int, int]]:
    queue = [(start_point, [start_point])]
    visited = {
        start_point
    }

    while queue:
        curr_pos, curr_route = queue.pop(0)
        neighbours = get_neighbours(maze, curr_pos[0], curr_pos[1])
        not_visited_neighbours = [neighbour for neighbour in neighbours if neighbour not in visited]
        for neighbour in not_visited_neighbours:
            if neighbour == end_point:
                return curr_route+[neighbour]
            visited.add(neighbour)
            queue.append((neighbour, curr_route+[neighbour]))
    raise ValueError("end point not reachable")


res = find_shortest_route(maze, start_point, end_point)
print(res)
