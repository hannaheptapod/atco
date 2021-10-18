n = input()
nr = ''.join(reversed(n))
length = len(n)
ans = 'No'
for _ in range(length + 1):
    if n == nr:
        ans = 'Yes'
        break
    n = '0'+n
    nr = nr+'0'
print(ans)