t = int(input())
for _ in range(t):
    n, c = input().split()
    n = int(n)
    s = input()
    s += s
    count = 0
    maxv = 0
    flag = 0
    for i in range(len(s)):
        if s[i] == c:
            flag = 1
        if s[i] == 'g':
            flag = 0
            maxv = max(maxv, count)
            count = 0
        if flag == 1:
            count += 1
    print(maxv)
