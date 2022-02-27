N = int(input())
S = input()

a, b = '', False
for si in S:
    if b:
        if si == 'A': a += 'A'
        elif si == 'B':
            a += 'A'
            b = False
        else:
            a += 'BC'
            b = False
    else:
        if si == 'A': a += 'A'
        elif si == 'B': b = True
        else: a += 'C'
if b: a += 'B'

print(a)