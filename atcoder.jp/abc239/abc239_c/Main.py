x1, y1, x2, y2 = map(int, input().split())

p = [
    [x1+2, y1+1],
    [x1+1, y1+2],
    [x1-1, y1+2],
    [x1-2, y1+1],
    [x1-2, y1-1],
    [x1-1, y1-2],
    [x1+1, y1-2],
    [x1+2, y1-1]
]
q = [
    [x2+2, y2+1],
    [x2+1, y2+2],
    [x2-1, y2+2],
    [x2-2, y2+1],
    [x2-2, y2-1],
    [x2-1, y2-2],
    [x2+1, y2-2],
    [x2+2, y2-1]
]

ans = 'No'

for pi in p:
    if pi in q: ans = 'Yes'

print(ans)