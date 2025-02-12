def squares(a,b):
    for i in range(a,b):
        yield i*i
a = int(input())
b = int(input())
for value in squares(a,b+1):
    print(value)