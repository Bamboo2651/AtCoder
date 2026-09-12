s = input()
n = len(s)

s_number = {}
s_pattern = []

for char in s:
    if char not in s_number:
        s_number[char] = len(s_number)

    s_pattern.append(s_number[char])
# print(s_number)
# print(s_pattern)

hani = 10 ** n

sosu = [True] * hani
sosu[0] = False
sosu[1] = False

for i in range(2, int(hani ** 0.5) + 1):
    if sosu[i]:
        for j in range(i * i,hani, i):
            sosu[j] = False
# print(sosu)


ans = -1

for p in range(2, hani):
    if sosu[p]:
        t = str(p)

        t_number = {}
        t_pattern = []

        for i in t:
            if i not in t_number:
                t_number[i] = len(t_number)

            t_pattern.append(t_number[i])
        if s_pattern == t_pattern:
            ans = p
            break

print(ans)