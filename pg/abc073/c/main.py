n = int(input())
p = set()
for _ in range(n):
    a = int(input())
    if a in p: p.remove(a)
    else: p.add(a)
print(len(p))