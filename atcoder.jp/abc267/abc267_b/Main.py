S = input()

lines = [any([S[i] == '1' for i in l]) for l in [[6], [3], [1, 7], [0, 4], [2, 8], [5], [9]]]

if S[0] == '0':
    for i in range(5):
        for j in range(i+2, 7):
            if lines[i] and lines[j]:
                for k in range(i+1, j):
                    if not lines[k]:
                        ans = 'Yes'
                        break
                else: continue
                break
        else: continue
        break
    else: ans = 'No'
else: ans = 'No'

print(ans)
