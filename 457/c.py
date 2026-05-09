n,k = map(int,input().split())
data = []
for _ in range(n):
    l = list(map(int,input().split()))
    l.pop(0)
    data.append(l)

c = list(map(int,input().split()))

b = []
for i in range(n):
    for j in range(c[i]):
        b.extend(data[i])

print(b[k-1])