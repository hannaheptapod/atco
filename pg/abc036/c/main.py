N = int(input())
a = [int(input()) for _ in range(N)]

comp = sorted(set(a))
dic = {v: i for i, v in enumerate(comp)}

ans = [dic[ai] for ai in a]
print(*ans, sep='\n')
