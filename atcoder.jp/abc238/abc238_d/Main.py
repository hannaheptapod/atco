T = int(input())

for _ in range(T):
    a, s = map(int, input().split())

    differ = s - 2*a

    if 2*a <= s and not differ&a: ans = 'Yes'
    else: ans = 'No'
    
    print(ans)