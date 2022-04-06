import datetime

now = datetime.date.today()

res = now.strftime('%Y-%m-%d')
sres = now.strftime('%Y/%m/%d')

print(res)
print(sres)

date = '2021-05-20'

 var = datetime.datetime.strptime(date, '%Y-%m-%d')
    # '%Y-%m-%d' : date의 포맷을 알려주는 코드

print(var)
print(var.year)

nex_var = var + datetime.timedelta(days=7) - datetime.timedelta(seconds =300)
print(nex_var)