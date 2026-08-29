n, k = map(int, input().split())
a = list(map(int, input().split()))

count = [0] * (k + 1)
for i in a:
    count[i] += 1

# print(count)
max_count = max(count[1:])
ans = 0
for i in count[1:]:
    if i + 1 >=max_count:
        ans += 1
print(ans)