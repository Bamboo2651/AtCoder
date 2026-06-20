ressya, X = input().split()
N = int(ressya)

target = "ABCDE".index(X)

for _ in range(N):
    S = input()
    if S[target] == "o":
        print("Yes")
        exit()
print("No")