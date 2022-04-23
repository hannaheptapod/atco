from string import ascii_lowercase, ascii_uppercase

S = input()
st = set(si for si in S)

if all([Ai not in st for Ai in ascii_uppercase]): ans = 'No'
elif all([ai not in st for ai in ascii_lowercase]): ans = 'No'
elif len(S) != len(st): ans = 'No'
else: ans = 'Yes'

print(ans)
