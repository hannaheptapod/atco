N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
b.sort()
xo = [a[0] ^ bi for bi in b]
ans = set()
for x in xo:
    c = [ai ^ x for ai in a]
    c.sort()
    if c == b:
        ans.add(x)
num = len(ans)
ans_l = list(ans)
ans_l.sort()
print(num)
if num > 0:
    _ = [print(an) for an in ans_l]