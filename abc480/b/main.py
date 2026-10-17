n, m = map(int, input().split())

s_box = []
for i in range(n):
    s_box.append(input())

t_box = []
for j in range(m):
    t_box.append(input())

count_box = [0] * n

for t in t_box:
    if t in s_box:
        i = s_box.index(t)
        count_box[i] += 1
        continue

    candidate_box = []

    for i in range(n):
        s = s_box[i]

        if len(s) != len(t):
            continue

        different_count = 0

        for j in range(len(s)):
            if s[j] != t[j]:
                different_count += 1

        if different_count == 1:
            candidate_box.append(i)

    if len(candidate_box) == 1:
        i = candidate_box[0]
        count_box[i] += 1

for count in count_box:
    print(count)