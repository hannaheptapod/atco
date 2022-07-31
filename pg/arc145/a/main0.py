N = int(input())
S = input()

if N == 2: ans = 'Yes' if S == S[::-1] else 'No'
elif N == 3: ans = 'Yes' if S in ('AAA', 'ABA', 'BAA', 'BAB', 'BBA', 'BBB') else 'No'
else:
    arr = list(S)
    if not N%2:
        if arr[N//2-1:N//2+1] == ['B', 'A']: arr[N//2-2:N//2+1] = ['A', 'B', 'B']
    for i in range(-int(-N//2)-1):
        if arr[i] == arr[-i-1]: continue
        elif i and arr[i-1:i+1] == ['A', 'A']: arr[i] = 'B'
        elif i and arr[i-1:i+1] == ['B', 'A']: arr[-i-1] = 'A'
        elif arr[i] == 'B': arr[-i-2:-i] = ['A', 'B']
        elif arr[-i-1] == 'A': arr[i:i+2] = ['A', 'B']
        else:
            ans = 'No'
            break
    else: ans = 'Yes'

print(ans)
