x = input()

ans = len(x)

sum_s = sum_t = 0
for xi in x:
    if xi == 'S': sum_s += 1
    elif sum_s:
        sum_s -= 1
        ans -= 2

print(ans)