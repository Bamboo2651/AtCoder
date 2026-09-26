q = int(input())
s = input()
t = input()

n = len(s)
m = len(t)

match = [0] * (n + 1)
# print(match)

for i in range(n - m + 1):
    if s[i:i + m] == t:
        match[i + 1] = 1

# print(match)

prefix = [0] * (n + 1)

for i in range(1, n + 1):
    prefix[i] = prefix[i - 1] + match[i]

# print(prefix)

for _ in range(q):
    l, r = map(int, input().split())

    last = r - m + 1

    if last < l:
        print("No")
    elif prefix[last] - prefix[l - 1] > 0:
        print("Yes")
    else:
        print("No")