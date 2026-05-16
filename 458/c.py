s = input()
resulut = 0

for i in range(len(s)):
    if s[i] == "C":
        leftlen = i
        rightlen = len(s) - i - 1
        
        minlen = min(leftlen, rightlen)
        resulut += minlen + 1

print(resulut)