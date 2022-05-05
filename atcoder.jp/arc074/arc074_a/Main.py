H, W = map(int, input().split())

ans = 0 if not H*W % 3 else min(H, W)

for i in range(1, H):
    ans = min(ans, max(-int(-W//2)*i, W*(H-i)) - min((W//2)*i, W*(H-i)))

    if ans: continue
    break
for j in range(1, W):
    ans = min(ans, max(-int(-H//2)*j, H*(W-j)) - min((H//2)*j, H*(W-j)))

    if ans: continue
    break

print(ans)
