a, b = map(int, input().split())
for i in range(100*100//8+1):
    if i*0.08//1 == a and i*0.1//1 == b:
        ans = i
        break
else: ans = -1
print(ans)