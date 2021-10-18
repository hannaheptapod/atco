n, k = map(int, input().split())
l = list(map(int, input().split()))
l_sort = sorted(l)
d = k % n
dic = {}
for i in range(d):
    dic[l_sort[i]] = (k // n) + 1
for j in range(d, n, 1):
    dic[l_sort[j]] = k // n
for i in range(n):
    print(dic.get(l[i]))
