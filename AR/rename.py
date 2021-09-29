import os

path = './'
dlt = 'AC'
files = os.listdir(path)
dirs = [file for file in files if os.path.isdir(os.path.join(path, file))]
for dir in dirs:
    p = os.path.join(path, dir)
    fs = os.listdir(p)
    ds = [f for f in fs if os.path.isdir(os.path.join(p, f))]
    for d in ds:
        if d[:2] == 'AC':
            d_new = d[2:]
            os.rename(os.path.join(p, d), os.path.join(p, d_new))