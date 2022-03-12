N, X = map(int, input().split())
S = input()
T = list(bin(X))
for si in S:
    if si == 'U':
        T.pop()
    elif si == 'L':
        T.append('0')
    else:
        T.append('1')

ans = int(''.join(T), 2)
print(ans)
