x = input()
alpha = 'abcdefghijklmnopqrstuvwxyz'
dict = {}
dictr = {}
for i in range(26):
    dict[alpha[i]] = x[i]
    dictr[x[i]] = alpha[i]

n = int(input())
list = []
for i in range(n):
    s = input()
    sr = str()
    for si in s:
        sr += dictr[si]
    list.append(sr)
list.sort()
for s in list:
    sr = str()
    for si in s:
        sr += dict[si]
    print(sr)