X = int(input())
Q = int(input())

kokuban = [X]
result = []
for _ in range(Q):
    A, B = map(int, input().split())
    kokuban.append(A)
    kokuban.append(B)
    kokuban.sort()
    midnum = len(kokuban) // 2

    result.append(kokuban[midnum])

for r in result:
    print(r)