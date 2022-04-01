s = input()
k = int(input())

if len(s) < k: ans = 0
else: ans = len(set(s[i:i+k] for i in range(len(s)-k+1)))

print(ans)
