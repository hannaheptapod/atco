x = float(input())
if x-int(x//1) < 0.5: print(int(x//1))
else: print(int(x//1)+1)