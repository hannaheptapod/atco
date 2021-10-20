h, w = map(int, input().split())
if h < 2 or w < 2: ans = 1
elif h//2 and w//2: ans = (h-1)*w//2 + (w+1)//2
else: ans = h*w // 2
print(ans)