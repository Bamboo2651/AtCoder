n, k = map(int, input().split())

a = [0] * n
ans = []


def search(i, nokori):
    num = i + 1

    if i == n - 1:
        if nokori % num == 0:
            a[i] = nokori // num
            ans.append(" ".join(map(str, a)))

        return

    for x in range(nokori // num + 1):
        a[i] = x
        search(i + 1, nokori - num * x)


search(0, k)

print("\n".join(ans))