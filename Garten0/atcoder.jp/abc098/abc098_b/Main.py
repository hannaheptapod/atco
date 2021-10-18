n = int(input())
s = input()
def count(str):
    s = set()
    for si in str:
        if si not in s: s.add(si)
    return s
ans = -1
for i in range(1, n):
    s1 = count(s[:i])
    s2 = count(s[i:])
    tmp = 0
    for si in s1:
        if si in s2: tmp += 1
    if tmp > ans: ans = tmp
print(ans)