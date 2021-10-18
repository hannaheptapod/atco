S = [input() for _ in range(4)]
ans = 'No'
if all(s in S for s in {'H', '2B', '3B', 'HR'}):
    ans = 'Yes'
print(ans)