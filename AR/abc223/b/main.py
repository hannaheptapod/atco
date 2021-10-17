s = input()
leng = len(s)
ls = []
for i in range(leng):
    ls.append(s)
    s = s[-1] + s[:leng-1]
ls.sort()
print(ls[0])
print(ls[-1])