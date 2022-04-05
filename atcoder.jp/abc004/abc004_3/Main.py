N = int(input())

deck = list(str(i) for i in range(1, 6+1))
for i in range(N%30): deck[i%5], deck[i%5 + 1] = deck[i%5 + 1], deck[i%5]

ans = ''.join(deck)
print(ans)
