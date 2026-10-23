n,q = map(int,input().split())
a = list(map(int,input().split()))
query = [list(map(int,input().split())) for _ in range(q)]

b = []
for i in range(n+1):
    for j in range(0,i):
        b.append(a[j])
print(b)
ans = 0
for i in range(q):
    l,r = query[i]
    for j in range(l-1,r):
        ans += b[j]
    print(ans)