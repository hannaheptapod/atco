A = int(input())


def N_to_Dec(digits, base):
    num = 0
    for digit in str(digits):
        num = num * base + int(digit)
    return num


i = 10
while True:
    tmp = N_to_Dec(i, i)
    if tmp < A:
        i += 1
        continue

    if tmp == A: ans = i
    else: ans = -1
    break

print(ans)
