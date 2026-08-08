N, Q = map(int, input().split())

values = [0] * N
positive_indices = set()
current_xor = 0

for _ in range(Q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        x = query[1] - 1

        old_value = values[x]
        values[x] += 1

        current_xor ^= old_value ^ values[x]
        positive_indices.add(x)

    else:
        for x in list(positive_indices):
            old_value = values[x]
            values[x] -= 1

            current_xor ^= old_value ^ values[x]

            if values[x] == 0:
                positive_indices.remove(x)

    print(current_xor)