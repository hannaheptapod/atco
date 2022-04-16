N = int(input())

dos = [1]
while True:
    if dos[-1]*2 >= N: break
    dos.append(dos[-1]*2)
id = len(dos) - 1

now, dir = 0, 1
print(now)
s = input()
while s != 'Vacant':
    now += dir * dos[id]
    now %= N
    print(now)

    last, s = s, input()
    if last != s: dir *= -1

    id -= 1
