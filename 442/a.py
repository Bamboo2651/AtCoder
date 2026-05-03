s = input()
count = 0
for i in range(len(s)):
    if s[i] == "i" or s[i] == "j" :
        count += 1

print(count)