from collections import deque

n, m, s, t = map(int, input().split())
g = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    g[a].append(b)

# print(g)

dist = [10 ** 9] * (n + 1)
dist[s] = 0
# print(dist)
dq = deque()
dq.append(s)              

while len(dq) > 0:
    u = dq.popleft()     
    # print(u, list(dist))
    if len(g[u]) == 0:
        continue
    mn = min(g[u])
    for v in g[u]:
        if v == mn:
            w = 0
        else:
            w = 1
        if dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
            # print(v, dist[v])
            if w == 0:
                dq.appendleft(v)   
            else:
                dq.append(v)       

if dist[t] == 10 ** 9:
    print(-1)
else:
    print(dist[t])