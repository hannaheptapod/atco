from bisect import bisect_left as bl
X = int(input())

leng = len(str(X))
st = set(i for i in range(10))

for i in range(10):
    for d in range(-i, 9-i + 1):
        tmp, now, cnt = 0, i, 0

        while now >= 0 and now < 10 and cnt <= leng:
            tmp = 10*tmp + now
            st.add(tmp)
            now += d
            cnt += 1

l = sorted(st)
ans = l[bl(l, X)]

print(ans)
