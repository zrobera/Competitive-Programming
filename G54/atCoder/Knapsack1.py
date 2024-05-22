N,W = map(int, input().split())

arr = []
ans = 0
for i in range(N):
    w,v = map(int, input().split())
    arr.append((w,v))
    
dp = [[0]*(W+1) for _ in range(N+1)]
for row in range(1,N+1):
    w,v = arr[row-1][0], arr[row-1][1]
    for curr_cap in range(W+1):
        if w <= curr_cap:
            dp[row][curr_cap] = max(v + dp[row-1][curr_cap-w], dp[row-1][curr_cap])
        else:
            dp[row][curr_cap] = dp[row-1][curr_cap]
print(dp[-1][-1])
 
