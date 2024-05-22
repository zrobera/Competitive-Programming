N = int(input())
matrix = []
dp = []
for i in range(N):
    arr = list(map(int, input().split()))
    matrix.append(arr)
    if i == 0:
        dp.append(arr)
    else:
        dp.append([0]*3)

for r in range(1,N):
    for c in range(3):
        for i in range(3):
            if i != c:
                dp[r][c] = max(dp[r][c], matrix[r][c] + dp[r-1][i])
print(max(dp[-1]))
