x1, y1, r = map(int, input().split())
x2, y2, x3, y3 = map(int, input().split())

if x1-r < x2 or x3 < x1+r or y1-r < y2 or y3 < y1+r: red = 'YES'
else: red = 'NO'

if max((x2-x1)**2, (x3-x1)**2) + max((y2-y1)**2, (y3-y1)**2) > r**2: blue = 'YES'
else: blue = 'NO'

print(red)
print(blue)