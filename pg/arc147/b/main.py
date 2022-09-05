import array
import random

N = int(input())
P = list(map(int, input().split()))

arr = array.array('i', [0]+P)
odd = [i for i in range(N+1) if not i%2 and arr[i]%2]
even = [i for i in range(N+1) if i%2 and not arr[i]%2]

ans = []
for _ in range(len(odd)):
    o, e = odd.pop(), even.pop()
    l, r = min(o, e), max(o, e)

    for i in range(l, r-2, 2):
        ans.append(('B', i))
        arr[i], arr[i+2] = arr[i+2], arr[i]
    ans.append(('A', r-1))
    arr[r-1], arr[r] = arr[r], arr[r-1]


def bubble_sort(data, head):
    change = True

    for i in range(len(data)):
        if not change: break
        change = False
        for j in range(len(data) - i -1):
            if data[j] > data[j+1]:
                ans.append(('B', 2*j + head))
                data[j], data[j+1] = data[j+1], data[j]
                change = True


bubble_sort(arr[0::2], 0)
bubble_sort(arr[1::2], 1)

print(len(ans))
_ = [print(*a) for a in ans]
