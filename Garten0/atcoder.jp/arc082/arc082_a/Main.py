n = int(input())
a = list(map(int, input().split()))
lst = [0]*(10**5 + 1)
for ai in a:
    lst[ai] += 1
    if ai > 0: lst[ai - 1] += 1
    if ai < 10**5: lst[ai + 1] += 1

ans = max(lst)
print(ans)