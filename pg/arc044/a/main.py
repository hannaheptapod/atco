N = int(input())

for i in range(2, int(N**0.5) + 1):
    if N%i: continue

    if N%10 in (1, 3, 7, 9) and sum(int(ni) for ni in list(str(N)))%3: ans = 'Prime'
    else: ans = 'Not Prime'

    break
else: ans = 'Prime' if N > 1 else 'Not Prime'

print(ans)
