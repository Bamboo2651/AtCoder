line1 = input()
N = int(line1)

line2 = input()
C_strings = line2.split()

C = []
for s in C_strings:
    C.append(int(s))

max_count = 0
for color in range(1, N + 1):
    count = 0
    for c in C:
        if c == color:
            count += 1
    
    if count > max_count:
        max_count = count

print(N - max_count)