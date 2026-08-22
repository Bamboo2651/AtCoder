from collections import deque

N, M, K = map(int, input().split())
A = list(map(int, input().split()))

recent_eaten = deque()
current_sum = 0

for i in range(N):
    if len(recent_eaten) == M:
        oldest = recent_eaten.popleft()
        current_sum -= oldest

    if current_sum + A[i] <= K:
        print("Yes")
        recent_eaten.append(A[i])
        current_sum += A[i]
    else:
        print("No")
        recent_eaten.append(0) 