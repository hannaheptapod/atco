a, b, c = map(int, input().split())
his = [[a, b, c]]
i = 0
while a%2 == 0 and b%2 == 0 and c%2 == 0:
    i += 1
    ta = (b + c) // 2
    tb = (c + a) // 2
    tc = (a + b) // 2
    a, b, c = ta, tb, tc
    if [a, b, c] in his:
        i = -1
        break
    else: his.append([a, b, c])
print(i)