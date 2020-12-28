A = [5,4,1,2,6,5]
B = [2]



def f(A=A, B=B):
    N, M = len(A), len(B)
    if N > 6*M or M > 6*N:
        return -1
    A.sort()
    B.sort()
    turned_dice = 0
    if sum(B) < sum(A):
        A, B = B, A     # WLOG sum(B) > sum(A)

    l, r = 0, len(B)-1  # pointers on A and B

    while sum(A) < sum(B):
        print(A,B)
        if l >= len(A):
            B[r] = 1
            r -= 1
        elif r < 0:
            A[l] = 6
            l += 1
        else:
            if A[l] < 7 - B[r]:
                A[l] = 6
                l += 1
            else:
                B[r] = 1
                r -= 1
        turned_dice += 1

    return turned_dice







print(f())
