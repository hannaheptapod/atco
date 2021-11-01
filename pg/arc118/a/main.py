t, n = map(int, input().split())
s = {i*(100+t)//100 for i in range(1, 100+1)}
l = [i for i in range(1, 100+t+1) if i not in s]
l.sort()
leng = len(l)
ans = (-int(-n//leng)-1)*(100+t) + l[n%leng - 1]
print(ans)