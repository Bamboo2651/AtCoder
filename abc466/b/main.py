N, M = map(int, input().split())

max_sizes = [-1] * (M + 1)

for _ in range(N):
    c, s = map(int, input().split())
    if s > max_sizes[c]:
        max_sizes[c] = s

ans = max_sizes[1 : M + 1]

print(*ans)