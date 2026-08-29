n = int(input())
s = input()

answer = 0

for i in range(n):
    if (
        s[i] == "x"
        and (i == 0 or s[i - 1] == "x")
        and (i == n - 1 or s[i + 1] == "x")
    ):
        answer += 1

print(answer)