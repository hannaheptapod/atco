from collections import Counter

S = input()
cnt = list(Counter(list(Counter(S).values())).items())

div = 0
for c, n in cnt:
    if c % 2: div += n

if div: ans = 2*((len(S)-div) // (2*div)) + 1
else: ans = len(S)
print(ans)
