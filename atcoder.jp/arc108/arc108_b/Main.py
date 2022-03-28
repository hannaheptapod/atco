import array

N = int(input())
s = input()

fox = array.array('i', [ord(c)-ord('a') for c in 'fox'])
t = array.array('i', [-1]*3)

ans = N
for si in s:
    t.append(ord(si)-ord('a'))

    if t[-3:] == fox:
        for _ in range(3): t.pop()
        ans -= 3

print(ans)
