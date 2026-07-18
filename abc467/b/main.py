n = int(input())

total = 0

for _ in range(n):
    user = input().split()
    
    a = int(user[0])
    b = int(user[1])
    s = user[2]
    
    if s == "keep":
        total += b-a

print(total)