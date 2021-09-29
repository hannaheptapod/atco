n = int(input())
s = [input() for _ in range(n)]
for i in range(n):
    if '#' in s[i]:
        top = i
        break
for i in range(n - 1, -1, -1):
    if '#' in s[i]:
        bottom = i
        break
for j in range(n):
    if '#' in [s[i][j] for i in range(top, bottom + 1)]:
        left = j
        break
for j in range(n - 1, -1, -1):
    if '#' in [s[i][j] for i in range(bottom, top - 1, -1)]:
        right = j
        break
t = [input() for _ in range(n)]
empty = '.'*n
for i in range(n):
    s[i] = empty + s[i] + empty
s = [empty*3 for _ in range(n)] + s + [empty*3 for _ in range(n)]
def rotate(s):
    si = [str() for _ in range(n)]
    for i in range(n):
        st = str()
        for j in range(n):
            st += s[j][n - 1 - i]
        si[i] = st
    return si
t1 = rotate(t)
t2 = rotate(t1)
t3 = rotate(t2)
tt = (t, t1, t2, t3)
ans = 'No'
for i in range(bottom + 1, n + top + 1):
    f = [s[y] for y in range(i, i + n)]
    for j in range(right + 1, n + left + 1):
        frame = [fi[j:j + n] for fi in f]
        if frame in tt:
            ans = 'Yes'
            break
    else: continue
    break
print(ans)