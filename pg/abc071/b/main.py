s = input()
st = {si for si in s}
alp = 'abcdefghijklmnopqrstuvwxyz'
for ai in alp:
    if ai not in st:
        print(ai)
        break
    else: continue
else: print('None')