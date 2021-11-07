s = input()
num = [0]*3
for si in s: num[{'a':0, 'b':1, 'c':2}[si]] += 1
if max(num)-min(num) <= 1: print('YES')
else: print('NO')