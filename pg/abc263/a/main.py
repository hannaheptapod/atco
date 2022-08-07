hands = map(int, input().split())

dic = {}
for h in hands:
    if h not in dic: dic[h] = 1
    else: dic[h] += 1

ans = 'Yes' if max(dic.values()) == 3 and min(dic.values()) == 2 else 'No'
print(ans)
