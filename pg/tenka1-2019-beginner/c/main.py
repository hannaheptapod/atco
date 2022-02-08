n = int(input())
s = input()

sm = sum([si == '.' for si in s])
ans = sm

for si in s:
    if si == '.': sm -= 1
    else: sm += 1
    ans = min(ans, sm)

print(ans)