s = input()
ans = ""
num = "0123456789"
for i in s:
    if i in num:
        ans += i

print(ans)