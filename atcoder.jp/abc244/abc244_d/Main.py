S = ''.join(input().split())
T = ''.join(input().split())

ord = ('RGB', 'RBG', 'GRB', 'GBR', 'BRG', 'BGR')
link = ('125', '034', '034', '125', '125', '034')

if str(ord.index(S)) in link[ord.index(T)]: ans = 'No'
else: ans = 'Yes'
print(ans)
