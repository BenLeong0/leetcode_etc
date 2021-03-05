from collections import defaultdict

def solution(g):
    # Transpose if longer than wide
    if len(g[0]) > len(g):
        g = [[g[i][j] for i in range(len(g))] for j in range(len(g[0]))]

    width, height = len(g[0]), len(g)

    def check(row_id,i,j):
        will_gas = (curr_grid[i][j]+curr_grid[i-1][j]+curr_grid[i][j-1]+curr_grid[i-1][j-1] == 1)
        is_gas = g[row_id][j-1]
        if (will_gas and is_gas) or ((not will_gas) and (not is_gas)):
            return True
        return False

    def backtrack(row_id,i=0,j=0):
        if j == width+1:
            a = convert_from_binary(curr_grid[0])
            b = convert_from_binary(curr_grid[1])
            curr_states[b] += prev_states[a]
        elif (i,j) == (0,0):
            backtrack(row_id,1,0)
            curr_grid[i][j] = 0
            backtrack(row_id,1,0)
        elif (i,j) == (1,0):
            backtrack(row_id,0,1)
            curr_grid[i][j] = 0
            backtrack(row_id,0,1)
            curr_grid[i][j] = 1
        elif i == 0:
            backtrack(row_id,1,j)
            curr_grid[i][j] = 0
            backtrack(row_id,1,j)
            curr_grid[i][j] = 1
        else:
            if check(row_id,i,j):
                backtrack(row_id,0,j+1)
            curr_grid[i][j] = 0
            if check(row_id,i,j):
                backtrack(row_id,0,j+1)
            curr_grid[i][j] = 1



    def convert_from_binary(row):
        return sum([value * 2**key for key,value in enumerate(row)])

    prev_states = {key:1 for key in range(2**(width+1))}
    for i in range(height):
        curr_grid = [[1]*(width+1) for _ in range(2)]
        curr_states = defaultdict(int)
        backtrack(i)
        prev_states=curr_states

    return sum(prev_states.values())

m = [[True, False, True], [False, True, False], [True, False, True]]
m = [[True, True, False, True, False, True, False, True, True, False], [True, True, False, False, False, False, True, True, True, False], [True, True, False, False, False, False, False, False, False, True], [False, True, False, False, False, False, True, True, False, False]]
# m = [[True, False, True, False, False, True, True, True], [True, False, True, False, False, False, True, False], [True, True, True, False, False, False, True, False], [True, False, True, False, False, False, True, False], [True, False, True, False, False, True, True, True]]
# m = [[True] * 45 for _ in range(9)]
print(solution(m))
