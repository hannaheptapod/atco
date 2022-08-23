S = input()

arr = list(S)
T = 'atcoder'

ans = 0
for i in range(7):
    id = arr.index(T[i])
    if id == i: continue

    arr[i:id+1] = [T[i]]+arr[i:id]
    ans += id - i

print(ans)
