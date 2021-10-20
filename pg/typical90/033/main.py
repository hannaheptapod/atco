h, w = map(int, input().split())
if h == 1 or w == 1:
    ans = h * w
else:
    ans = (-h//2)*(-w//2)
print(ans)