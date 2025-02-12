import datetime 
x = datetime.datetime.now()
y = x - datetime.timedelta(days=1)
z = x - datetime.timedelta(days=-1)
print(y)
print(x)
print(z)