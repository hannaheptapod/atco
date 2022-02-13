sx, sy, tx, ty = list(map(int, input().split()))

xd, yd = tx-sx, ty-sy
ru, ld = 'R'*xd + 'U'*yd, 'L'*xd + 'D'*yd

ans = ru + ld + 'DR'+ru+'UL' + 'UL'+ld+'DR'

print(ans)