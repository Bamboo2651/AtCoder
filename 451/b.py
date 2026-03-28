N,M = map(int,input().split())
now_count = {}
next_count = {}
data = []
for i in range(N):
    AB =list(map(int,input().split()))
    data.append(AB)

for i in range(N):
    a = data[i][0]
    b = data[i][1]
    
    if a not in now_count:
        now_count[a] = 0
    now_count[a] += 1
    if b not in next_count:
        next_count[b] = 0
    next_count[b] += 1

for i in range(1,M+1):
    if i in next_count:
        next = next_count[i]
    else:
        next = 0
    
    if i in now_count:
        now = now_count[i]
    else:
        now = 0

    print(next - now)

