n = int(input())
s = input()
t = input()
for i in range(n):
    if t[i] != "*" and s[i] != t[i]:
        print("No")
        break
else:
    print("Yes")