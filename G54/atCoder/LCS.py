s = input()
t = input()
dp = [[0]*(len(s)+1) for _ in range(len(t)+1)]

for r in range(len(t)-1,-1,-1):
    for c in range(len(s)-1,-1,-1):
        if t[r] == s[c]:
            dp[r][c] = 1 + dp[r+1][c+1]
        else:
            dp[r][c] = max(dp[r+1][c], dp[r][c+1])
            
ans = []
i,j = 0,0

while i < len(t) and j < len(s):
        if t[i] == s[j]:
            ans.append(t[i])
            i += 1
            j += 1
        else:
            if dp[i+1][j] > dp[i][j+1]:
                i += 1
            else:
                j += 1
                
print("".join(ans))

            

