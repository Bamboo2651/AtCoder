n, m = map(int, input().split())

counts = [0] * n

person = 0

for _ in range(m):
    counts[person] += 1
    person += 1

    if person == n:
        person = 0
print(*counts)