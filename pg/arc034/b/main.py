N = int(input())


def f(x): return sum(map(int, list(str(x))))


ans = [0]
for x in range(max(1, N-153), N):
    if x + f(x) == N: ans.append(x)
ans[0] = len(ans) - 1

print(*ans, sep='\n')
