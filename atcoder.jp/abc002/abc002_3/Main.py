xa, ya, xb, yb, xc, yc = map(int, input().split())

ans = abs((xa-xb)*(ya-yc) - (ya-yb)*(xa-xc)) / 2
print(ans)
