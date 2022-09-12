import sys
import os
import json

DIR_P = 'py'
DIR_J = '/Users/jink/Programme/proc/.vscode/atcoder.code-snippets'

args = sys.argv
if len(args) > 1: files = args[1:]
else: files = [f[:-3] for f in os.listdir(DIR_P) if os.path.isfile(os.path.join(DIR_P, f)) and f.endswith('.py')]

for file in files:
    with open('py/'+file+'.py') as src: body = src.read().splitlines()
    with open(DIR_J, 'r') as f: snippets = json.load(f)
    snippets[file] = {"prefix": file, "body": body, "description": file}
    with open(DIR_J, 'w') as f: json.dump(snippets, f, indent=4, sort_keys=True)
