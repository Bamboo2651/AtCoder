s = input()
b = input()

if (
    s[0] == "A" and s[1] == "D"
    or s[0] == "D" and s[1] == "A"
    or b[0] == "A" and b[1] == "D"
    or b[0] == "D" and b[1] == "A"
    or s[0] == "A" and b[0] == "D"
    or s[0] == "D" and b[0] == "A"
    or s[1] == "A" and b[1] == "D"
    or s[1] == "D" and b[1] == "A"
):
    print("Yes")
else:
    print("No")