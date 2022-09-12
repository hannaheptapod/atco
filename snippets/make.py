import sys
from pyperclip import copy

args = sys.argv
name = input('Input the name of snippet:') if len(args) == 1 else args[1]

try:
    with open('py/'+name+'.py') as src: l = map(lambda x: '        "'+x[:-1]+'",', src.readlines())
    with open('txt/'+name+'.txt', mode='w') as txt:
        txt.write('"'+name+'": {\n')
        txt.write('    "prefix": "'+name+'",\n')
        txt.write('    "body": [\n')
        txt.write('\n'.join(l))
        txt.write('\n    ],\n')
        txt.write('},')
    with open('txt/'+name+'.txt') as src: copy(''.join(src.readlines()))
except Exception as e: print(e)
else: print('The operation is successful. The snippet has been copied to the clipboard.')
