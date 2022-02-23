S = input()

i, cnt, ans = 0, 0, 0
while i < len(S)-1:
    if S[i:i+2] == '25':
        cnt += 1
        i += 2
    else:
        ans += cnt*(cnt + 1)//2
        cnt = 0
        i += 1
ans += cnt*(cnt + 1)//2

print(ans)