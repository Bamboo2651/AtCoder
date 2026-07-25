n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

f = [1] * (n + 1)
for i in range(1, n + 1):
    f[i] = f[i - 1] * i

p_rank = 0
boxp = list(range(1, n + 1))
for i in range(n):
    idx = boxp.index(p[i])
    p_rank += idx * f[n - 1 - i]
    boxp.remove(p[i])

q_rank = 0
boxq = list(range(1, n + 1))
for i in range(n):
    idx = boxq.index(q[i])
    q_rank += idx * f[n - 1 - i]
    boxq.remove(q[i])

if p_rank < q_rank:
    ans = q_rank - p_rank - 1
else:
    ans = 0

print(ans)