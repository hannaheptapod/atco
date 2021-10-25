s = input()
if any(['N' in s and 'S' not in s, 'N' not in s and 'S' in s, 'E' in s and 'W' not in s, 'W' in s and 'E' not in s]): ans = 'No'
else: ans = 'Yes'
print(ans)