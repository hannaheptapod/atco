h = int(input())
dos = 2
for i in range(1, 41):
    if h < dos: 
        print(2**i - 1)
        break
    else:
        dos *= 2