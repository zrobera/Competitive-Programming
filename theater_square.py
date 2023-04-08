import math

n, m, a = map(int, input().split())

rows = math.ceil(n / a)
cols = math.ceil(m / a)

total = rows * cols

print(total)
