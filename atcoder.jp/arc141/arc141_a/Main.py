T = int(input())

for _ in range(T):
    s = input()

    ans = 11
    for p in range(1, len(s)//2+1):
        if len(s)%p: continue

        if int(s[:p]*(len(s)//p)) <= int(s): ans = max(ans, int(s[:p]*(len(s)//p)))
        elif int(s[:p]) > 10**(p-1): ans = max(ans, int(str(int(s[:p])-1)*(len(s)//p)))
        else: ans = max(ans, int('9'*(len(s)-1)))
    print(ans)
