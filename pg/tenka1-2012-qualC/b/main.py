import re

s = input()
deck = re.split('(?=[SHDC])', s)[1:]

ans = ''
cnt = len(deck)
for soot in 'SHDC':
    ta = ''
    tc = 0
    rsf = {soot+num for num in ('10', 'J', 'Q', 'K', 'A')}

    for card in deck:
        if card not in rsf:
            ta += card
            tc += 1
        else:
            rsf.remove(card)
            if not rsf: break
    else: continue

    if tc < cnt:
        ans = ta
        cnt = tc

print(ans if cnt else cnt)
