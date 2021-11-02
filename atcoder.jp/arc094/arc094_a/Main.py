a, b, c = sorted(list(map(int, input().split())))
ans = (b-a)//2 + 2*((b-a)%2) + c-b
print(ans)