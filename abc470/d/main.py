N, Q = map(int, input().split())

P = [0] + list(map(int, input().split()))
inverse = [0] * (N + 1)

for i in range(1, N + 1):
    inverse[P[i]] = i

for _ in range(Q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        x = query[1]
        y = query[2]

        value_x = P[x]
        value_y = P[y]

        P[x], P[y] = P[y], P[x]

        inverse[value_x] = y
        inverse[value_y] = x

    else:
        P, inverse = inverse, P

print(*P[1:])