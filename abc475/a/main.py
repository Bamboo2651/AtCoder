s = input()
ans = ""
for i in range(len(s)):
    if i != len(s)-1:
        ans += s[i] + "o"
    else:
        ans += s[i]
print(ans)
    