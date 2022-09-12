N, K = map(int, input().split())
S = input()

rle = [[0, 0, 0]] + [[S[0], 1, 1]]
for si in S[1:]:
    if rle[-1][0] == si: rle[-1][1], rle[-1][2] = rle[-1][1]+1, rle[-1][2]+1
    else: rle.append([si, 1, rle[-1][-1]+1])

ans = 0
for l in range(len(rle)-1):
    r = min(l+2*K+1 if rle[l+1][0] == '1' else l+2*K, len(rle)-1)
    ans = max(ans, rle[r][-1]-rle[l][-1])

print(ans)
