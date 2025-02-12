def rev(n):
    while n > 0:
        n = n - 1
        yield n
n = int(input())
for i in rev(n):
    print(i)