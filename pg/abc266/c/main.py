P = [list(map(int, input().split())) for _ in range(4)]

for i in range(4):
    a = (P[i%4][0]-P[(i-1)%4][0], P[i%4][1]-P[(i-1)%4][1])
    b = (P[(i+1)%4][0]-P[i%4][0], P[(i+1)%4][1]-P[i%4][1])

    if a[0]*b[1] - a[1]*b[0] <= 0:
        ans = 'No'
        break
else: ans = 'Yes'

print(ans)
