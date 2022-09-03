N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())


def calc(i, j): return abs(i-A) == abs(j-B)


arr = [['#' if calc(i, j) else '.' for j in range(R, S+1)] for i in range(P, Q+1)]

_ = [print(''.join(ai)) for ai in arr]
