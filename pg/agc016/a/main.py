s = input()
ls= len(s)
st = set(s)
ans = ls-1
for sti in st:
    id = [i for i in range(ls) if s[i] == sti]
    d = [id[0]] + [id[i+1]-id[i]-1 for i in range(len(id)-1)] + [ls-id[-1]-1]
    ans = min(ans, max(d))
print(ans)