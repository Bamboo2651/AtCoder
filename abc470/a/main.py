n = int(input())
for i in range(1, n + 1):
    if i % 3 == 0:
        result = "Fizz"
    else:
        result = str(i)
    print(result)