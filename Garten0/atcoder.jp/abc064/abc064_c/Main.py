n = int(input())
a = list(map(int, input().split()))
rates = [0] * 9
for ai in a:
    color = ai // 400
    if color < 8 and rates[color] == 0: rates[color] = 1
    elif color >= 8: rates[8] += 1

if sum(rates[:8]) == 0: print(1, rates[8])
else: print(sum(rates[:8]), sum(rates))