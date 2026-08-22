
S = input()
ans = ""

for char in S:
    if char == "A":
        ans += char
    else:
        ans += "."

print(ans)