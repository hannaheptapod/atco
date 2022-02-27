from collections import Counter
import array

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

C_a, C_b = Counter(A), Counter(B)
if C_a != C_b: ans = 'No'
elif any([c > 1 for c in C_a.values()]): ans = 'Yes'
else:
    arr = array.array('i', A)

    for i in range(N-2):
        for j in range(N-1, i-1, -1):
            if arr[j] == B[i]:
                k = j
                break
        for j in range(k, i+1, -2):
            arr[j-2], arr[j-1], arr[j] = arr[j], arr[j-2], arr[j-1]

        if arr[i] != B[i]:
            arr[i], arr[i+1], arr[i+2] = arr[i+1], arr[i+2], arr[i]

    a1 = list(arr)

    if a1 == B: ans = 'Yes'
    else: ans = 'No'

print(ans)