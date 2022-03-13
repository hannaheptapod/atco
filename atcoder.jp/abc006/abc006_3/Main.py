N, M = map(int, input().split())

if M < 2*N or M > 4*N:
    (a, b, c) = (-1, -1, -1)
else:
    c = (M - 2*N)//2
    b = (M - 2*N) % 2
    a = N - b - c

print(a, b, c)
