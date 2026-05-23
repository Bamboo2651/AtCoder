import re

N = int(input())
words = input().split()

result = []
for s in words:
    if re.match(r"[abc]", s):
        result.append("2")
    elif re.match(r"[def]", s):
        result.append("3")
    elif re.match(r"[ghi]", s):
        result.append("4")
    elif re.match(r"[jkl]", s):
        result.append("5")
    elif re.match(r"[mno]", s):
        result.append("6")
    elif re.match(r"[pqrs]", s):
        result.append("7")
    elif re.match(r"[tuv]", s):
        result.append("8")
    elif re.match(r"[wxyz]", s):
        result.append("9")

for i in result:
    print(i, end="")

