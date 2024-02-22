t= int(input())

for _ in range(t):
    n= int(input())
    s= input()
    prefix_sum = 0
    dictt = {0:1}
    ans = 0
    
    for i in range(len(s)):
        prefix_sum += int(s[i])
        ans += dictt.get(prefix_sum-i-1,0)
        dictt[prefix_sum-i-1]  = dictt.get(prefix_sum-i-1,0) + 1
    print(ans)