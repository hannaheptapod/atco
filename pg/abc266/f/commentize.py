print('txt file:')
f = open(input(), 'r', encoding='UTF-8')

data = f.readlines()
for i in range(len(data)): data[i] = '"' + data[i][:-1] + '",\n'

f.close()

with open('output.txt', 'w') as f:
    f.writelines(data)
    f.close()
