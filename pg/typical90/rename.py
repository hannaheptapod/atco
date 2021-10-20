import os

path = './'
dlt = 'AC'
files = os.listdir(path)
dirs = [file for file in files if os.path.isdir(os.path.join(path, file))]
for dir in dirs:
    if dir[:2] == 'AC':
        p = os.path.join(path, dir)
        pp = os.path.join(path, dir[2:])
        os.rename(p, pp)