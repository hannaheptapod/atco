R, C = map(int, input().split())

print('black' if min(min(R, 16-R), min(C, 16-C))%2 else 'white')
