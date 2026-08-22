N = int(input())
L = list(map(int, input().split()))

total = sum(L)

left_sum = 0

min_diff = float("inf")

for i in range(N - 1):
    left_sum += L[i]
    right_sum = total - left_sum

    diff = abs(left_sum - right_sum)

    if diff < min_diff:
        min_diff = diff

print(min_diff)