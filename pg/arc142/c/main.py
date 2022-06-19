N = int(input())

d = [0]*(N+1)

mn, id = N, []
for i in range(3, N+1):
    for j in (1, 2):
        q = ['?', i, j]
        print(*q)
        d[i] += int(input())

    mn = min(mn, d[i])
    if d[i] == 3: id.append(i)

if mn != 3: ans = mn
elif len(id) != 2: ans = 1
else:
    q = ['?']+id
    print(*q)
    dxy = int(input())
    ans = 1 if dxy in (2, 3) else 3

print('!', ans)
