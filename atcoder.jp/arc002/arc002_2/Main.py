import datetime

YMD = input()

date = datetime.datetime.strptime(YMD, '%Y/%m/%d')
y, m, d = map(int, YMD.split('/'))

while y%(m * d):
    date += datetime.timedelta(days=1)
    y, m, d = [int(format(date, ymd)) for ymd in ('%Y', '%m', '%d')]

print(format(date, '%Y/%m/%d'))