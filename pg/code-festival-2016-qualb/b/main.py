n, a, b = map(int, input().split())
s = input()
na = nb = 0
for si in s:
    if si == 'a':
        if na + nb < a + b:
            print('Yes')
            na += 1
        else: print('No')
    elif si == 'b':
        if na + nb < a + b and nb < b:
            print('Yes')
            nb += 1
        else: print('No')
    else: print('No')