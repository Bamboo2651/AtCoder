s = input()
e_count = s.count('E')
w_count = s.count('W')

if e_count > w_count:
    print("East")
else:
    print("West")