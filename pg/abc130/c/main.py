w, h, x, y = map(int, input().split())
if x*2==w and y*2==h: a2 = 1
else: a2 = 0
print(w*h / 2, a2)