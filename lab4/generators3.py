def gen(n):
    for i in range(n+ 1):
        if i % 3 == 0 or i % 4 == 0:
            yield i
n = int(input())
for value in gen(n):
    print(value)