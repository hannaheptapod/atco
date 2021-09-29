s = input()
sr = s[::-1]
l = len(s)
drow = {'maerd', 'remaerd', 'esare', 'resare'}

i = 0
while i < l:
    for d in drow:
        if sr[i:i+len(d)] == d:
            i += len(d)
            break
    else:
        break

if i == l:
    ans = 'YES'
else:
    ans = 'NO'

print(ans)