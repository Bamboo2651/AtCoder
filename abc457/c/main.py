n, k = map(int, input().split())

a = []
lengths = []

for _ in range(n):
    r = list(map(int, input().split()))

    li = r[0]
    ai = r[1:]

    lengths.append(li)
    a.append(ai)

c = list(map(int, input().split()))

# K番目がどのリストに入っているかを探す
for i in range(n):
    block_size = lengths[i] * c[i]

    if k > block_size:
        k -= block_size
    else:
        index = (k - 1) % lengths[i]
        ans = a[i][index]

        print(ans)
        break