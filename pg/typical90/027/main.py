n = int(input())
s = set()
ans = set()
for i in range(n):
    st = input()
    if st not in s:
        s.add(st)
        ans.add(i+1)
_ = [print(a) for a in ans]