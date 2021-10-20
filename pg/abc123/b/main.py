list = [int(input()) for _ in range(5)]
ans = 0
mod = []
for l in list:
    ans += l
    mod.append((10-l) % 10)
ans += sum(mod) - max(mod)
print(ans)