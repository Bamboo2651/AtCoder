n =int(input())
data = []
for _ in range(n):
    l = list(map(int,input().split()))
    l.pop(0)
    data.append(l)

x,y = map(int,input().split())
print(data[x-1][y-1])