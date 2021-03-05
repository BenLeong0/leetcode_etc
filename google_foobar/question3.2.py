from fractions import Fraction as frac

def solution(m):
    # https://brilliant.org/wiki/absorbing-markov-chains/
    n = len(m)
    terminals = []
    nonterminals = []
    for i in range(n):
        if sum(m[i]) == 0:
            terminals.append(i)
        else:
            nonterminals.append(i)

    # If only one terminal
    if len(terminals) == 1:
        return [1,1]
    # If 0 is a terminal
    if terminals[0] == 0:
        return [1] + [0]*(len(terminals)-1) + [1]

    Q = [[ frac( m[i][j] , sum(m[i]) ) for j in nonterminals] for i in nonterminals]
    R = [[ frac( m[i][j] , sum(m[i]) ) for j in terminals] for i in nonterminals]

    I = [[0 for _ in range(len(Q))] for _ in range(len(Q))]
    for i in range(len(I)):
        I[i][i] = 1
    N = [[I[i][j] - Q[i][j] for j in range(len(Q))] for i in range(len(Q))]

    def transposeMatrix(m):
        # return map(list,zip(*m))
        return list(map(list,zip(*m))) # Python3

    def getMatrixMinor(m,i,j):
        return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

    def getMatrixDeternminant(m):
        #base case for 2x2 matrix
        if len(m) == 2:
            return m[0][0]*m[1][1]-m[0][1]*m[1][0]

        determinant = 0
        for c in range(len(m)):
            determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
        return determinant

    def getMatrixInverse(m):
        determinant = getMatrixDeternminant(m)
        #special case for 2x2 matrix:
        if len(m) == 2:
            return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                    [-1*m[1][0]/determinant, m[0][0]/determinant]]

        #find matrix of cofactors
        cofactors = []
        for r in range(len(m)):
            cofactorRow = []
            for c in range(len(m)):
                minor = getMatrixMinor(m,r,c)
                cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
            cofactors.append(cofactorRow)
        cofactors = transposeMatrix(cofactors)
        for r in range(len(cofactors)):
            for c in range(len(cofactors)):
                cofactors[r][c] = cofactors[r][c]/determinant
        return cofactors

    N = getMatrixInverse(N)

    def multiply_matrices(m,n):
        if len(m[0]) != len(n):
            print('nope')
            return False
        return [[sum([m[i][k]*n[k][j] for k in range(len(m[0]))]) for j in range(len(n[0]))] for i in range(len(m))]

    M = multiply_matrices(N,R)
    result = M[0]

    while not all([x.denominator == 1 for x in result]):
        max_denom = max(result, key=lambda x:x.denominator).denominator
        result = [x*max_denom for x in result]
    result = [int(x) for x in result]
    result.append(sum(result))
    return result



m = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
m = [[0,2,1,0,0],[2,0,1,1,0],[1,2,0,0,1],[0,0,0,0,0],[0,0,0,0,0]]
m = [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]]
# m = [[1, 1, 1, 1, 1,],  [0, 0, 0, 0, 0,], [1, 1, 1, 1, 1,], [0, 0, 0, 0, 0,], [1, 1, 1, 1, 1,] ]
# m = [[0,0,0,0,0],[1,0,1,0,0],[0,1,0,1,0],[0,0,1,0,1],[0,0,0,0,0]]
print(solution(m))



# def solution(m):
#     terminals = {}
#     max_denom = 1
#     for i in range(len(m)):
#         if sum(m[i]) == 0:
#             terminals[i] = []
#         else:
#             max_denom *= sum(m[i])
#     if len(terminals) == 1:
#         return [1,1]
#
#     # DFS with repeats
#     visited = set()         # [num, den]
#     def rec(curr=0,curr_prob=[1,1]):
#         # If terminal, save probabilty (num and den)
#         if curr in terminals:
#             terminals[curr].append(curr_prob)
#             return
#
#         # Else explore children
#         visited.add(curr)
#         curr_den = sum(m[curr]) * curr_prob[1]
#         for j in range(len(m)):
#             if m[curr][j] != 0 and j not in visited:
#                 rec(j,[curr_prob[0]*m[curr][j],curr_den])
#         visited.remove(curr)
#
#     rec()
#
#     # Normalise probabilities and extract
#     for terminal in terminals:
#         if terminals[terminal]:
#             terminals[terminal] = sum([x[0]*max_denom//x[1] for x in terminals[terminal]])
#         else:
#             terminals[terminal] = 0
#     terminal_values = list(terminals.values())
#
#     # Find hcf of probabilities and divide through
#     def find_hcf(x,y):
#         while(y):
#             x, y = y, x % y
#         return x
#     hcf = find_hcf(terminal_values[0], terminal_values[1])
#     for i in range(2,len(terminal_values)):
#         hcf = find_hcf(hcf, terminal_values[i])
#     terminal_values = [x//hcf for x in terminal_values]
#
#     # Append denominator
#     terminal_values.append(sum(terminal_values))
#     return terminal_values
