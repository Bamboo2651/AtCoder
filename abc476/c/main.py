n = int(input())
a = list(map(int, input().split()))


top = a[:3]
# print(top)
top.sort(reverse=True)
# print(top)

first = top[0]
second = top[1]
third = top[2]


print(third)

for i in range(3,n):
    x = a[i]

    if x > first:
        third = second
        second = first
        first = x
    elif x > second:
        third = second
        second = x
    elif x > third:
        third = x

    print(third)