c = input()
mother = {'a', 'e', 'i', 'o', 'u'}
ans = 'consonant'
if any(c == m for m in mother):
    ans = 'vowel'
print(ans)