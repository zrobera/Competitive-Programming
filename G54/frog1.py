N = int(input())
arr = list(map(int, input().split()))
dp = [0]*N
dp[N-2] = abs(arr[-1] - arr[-2])

for i in range(N-3,-1,-1):
    dp[i] = min(
        dp[i+1]+abs(arr[i+1] - arr[i]),
        dp[i+2]+abs(arr[i+2] - arr[i])
        )
print(dp[0])