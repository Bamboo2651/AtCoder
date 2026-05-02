s = input()
box = []
curry = []

for i in range(len(s)):
    curry.append(s[i])
    
    if i + 1 < len(s):
        if s[i] == s[i+1]:
            box.append(curry)
            curry = []
    else:
        box.append(curry)
# print(box)

total = 0
ans = 0
for i in box:
    n = len(i)
    total = n * (n + 1) //2
    ans += total
print(ans)