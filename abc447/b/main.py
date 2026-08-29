s = input()
box = [0] * 26
for c in s:
    index = ord(c) - ord("a")
    box[index] += 1

# print(max(box))
ans = ""
for c in s:
    index = ord(c) - ord("a")

    if box[index] != max(box):
        ans += c

print(ans)