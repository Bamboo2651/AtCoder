
# n = int(input())

# box = []
# for _ in range(n):
#     h, l = map(int, input().split())
#     box.append([h, l])

# q = int(input())
# l = list(map(int, input().split()))

# TLEコード
# for ti in l:
#     ans = 0
#     for h, l in box:
#         if l > ti:
#             ans = max(ans,h)
#     print(ans)


# TLE回避コード
from bisect import bisect_right

n = int(input())

box = []
l_list = []

for _ in range(n):
    h, l = map(int, input().split())
    box.append([h, l])
    l_list.append(l)

# max_h[i] = box[i]から右側にいる人の最大身長
max_h = [0] * n
max_h[-1] = box[-1][0]

for i in range(n - 2, -1, -1):
    max_h[i] = max(box[i][0], max_h[i + 1])

q = int(input())
t_list = list(map(int, input().split()))

for t in t_list:
    idx = bisect_right(l_list, t)
    print(max_h[idx])

