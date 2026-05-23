N, Q = map(int, input().split())
blocks = [0] * (N + 1)
answers = []

for _ in range(Q):
    query = list(map(int, input().split()))
    q_type = query[0]
    val = query[1]

    if q_type == 1:
        x = val
        blocks[x] += 1

        min_val = min(blocks[1 : N + 1])
        if min_val > 0:
            for i in range(1, N + 1):
                blocks[i] -= min_val

    elif q_type == 2:
        y = val
        count = 0
        for i in range(1, N + 1):
            if blocks[i] >= y:
                count += 1
        answers.append(count)

for ans in answers:
    print(ans)