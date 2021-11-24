x = int(input())
ans = 2 * (x//11)
if x%11 == 0: ans += 0
elif x%11 <= 6: ans += 1
else: ans += 2
print(ans)