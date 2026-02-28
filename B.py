入力された文字の最も多いいしゅちゅ剣する文字を取り除いて出力する
a = input()
b = {}
for i in a:
    if i in b:
        b[i] += 1
    else:
        b[i] = 1

max_count = 0

for i in b:
    if b[i] > max_count:
        max_count = b[i]
        max_char = i

result = ""
for i in a:
    if i != max_char:
        result += i
print(result)