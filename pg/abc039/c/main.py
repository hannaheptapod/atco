S = input()
T = 'WBWBWWBWBWBWWBWBWWBWBWBWWBWBWWB'
for i in range(12):
    if S[:12] == T[i:i+12]: break

dic = {
    0: 'Do',
    2: 'Re',
    4: 'Mi',
    5: 'Fa',
    7: 'So',
    9: 'La',
    11: 'Si'
}

ans = dic[i]
print(ans)
