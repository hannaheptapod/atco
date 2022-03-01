from calendar import c


T = int(input())

for _ in range(T):
    N = int(input())
    S = [input()*2 for _ in range(3)]

    print('0'*N + '1'*N + '0')