import sys
import os
import json

args = sys.argv
DIR_J = '/Users/jink/Programme/proc/.vscode/atcoder.code-snippets'
DIR_S = 'src/'

with open(DIR_J, 'r') as f: snippets = json.load(f)

if len(args) > 1: snips = args[1:]
else: snips = [f[:-3] for f in os.listdir(DIR_S) if os.path.isfile(os.path.join(DIR_S, f)) and f.endswith('.py')]

for snip in snips:
    with open(DIR_S+snip+'.py') as py: body = py.read().splitlines()

    if os.path.isfile(DIR_S+snip+'.txt'):
        with open(DIR_S+snip+'.txt') as des: description = des.read().splitlines()
    else: description = [snip]

    snippets[snip] = {"body": body, "description": description, "prefix": snip}

with open(DIR_J, 'w') as f: json.dump(snippets, f, indent=4, sort_keys=True)
