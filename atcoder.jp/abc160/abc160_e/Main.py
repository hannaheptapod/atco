from audioop import reverse


x, y, _, _, _ = map(int, input().split())
p, q, r = [list(map(int, input().split())) for _ in range(3)]
_ = [l.sort(reverse=True) for l in (p, q)]

ans = sum(sorted(p[:x]+q[:y]+r, reverse=True)[:x+y])

print(ans)