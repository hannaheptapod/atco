x, y, W = input().split()
x, y = map(lambda i: int(i)+7, (x, y))
c = [input() for _ in range(9)]

c = [ci[:0:-1] + ci + ci[-2::-1] for ci in c]
c = c[:0:-1] + c + c[-2::-1]

pos = [[y, y, y, y], [x, x, x, x]]
if 'R' in W: pos[1] = [x, x+1, x+2, x+3]
if 'L' in W: pos[1] = [x, x-1, x-2, x-3]
if 'U' in W: pos[0] = [y, y-1, y-2, y-3]
if 'D' in W: pos[0] = [y, y+1, y+2, y+3]

ans = ''.join([c[pos[0][i]][pos[1][i]] for i in range(4)])
print(ans)
