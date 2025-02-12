n = int(input())
l = []
for i in range(n):
    if i % 2 == 0:
        l.append(i)
output = ", ".join(map(str, l))
print(output)
