s = input()
ans = 0
length = 0

for i in range(len(s)):
    if s[i] == s[i-1]:
        length = 1
    else:
        length += 1
    ans += length
print(ans%998244353)