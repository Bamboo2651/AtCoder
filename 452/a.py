m, d = map(int, input().split())

if (m == 1 and d == 7) or (m == 3 and d == 3) or (m == 5 and d == 5) or (m == 7 and d == 7) or (m == 9 and d == 9):
    print("Yes")
else:
    print("No")