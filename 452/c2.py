n = int(input())
rokkotu = []
for _ in range(n):
    ab = list(map(int,input().split()))
    rokkotu.append(ab)


m =int(input())
sbox = []
for _ in range(m):
    s = input()
    sbox.append(s)
# print(rokkotu)
# print(sbox)


kouho = [set() for _ in range(n)]
for i in range(n):
    for j in range(m):
        if rokkotu[i][0] != len(sbox[j]):
            continue
        else:
            kouho_moji = sbox[j]
            kouho_2 = kouho_moji[rokkotu[i][1]-1]
            kouho[i].add(kouho_2)

# print(kouho)


for i in range(m):
    if len(sbox[i]) != n:
        print("No")
        continue
    
    for j in range(n):
        one_moji =sbox[i]
        one_moji =one_moji[j]
        if one_moji not in kouho[j]:
            print("No")
            break
    else:
        print("Yes")
    