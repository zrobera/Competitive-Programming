N,K = map(int, input().split())
arr = list(map(int, input().split()))

dp = [float('inf')]*N
dp[N-1] = 0

for i in range(N-2,-1,-1):
    if K + i >= N-1:
        dp[i] = abs(arr[-1] - arr[i])
    else:
        j = 1
        while j <= K and i+j < N:
            dp[i] = min(dp[i],dp[i+j] + abs(arr[i+j] - arr[i]))
            j += 1
              
print(dp[0])
