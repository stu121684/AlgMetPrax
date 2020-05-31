from sys import stdin

n,m = map(int, stdin.readline().split())
x = list(map(int, stdin.readline().split()))

maxDeathPerTimeSlice = [0]*n
for i in range(m,n):
    maxDeathPerTimeSlice[i] = max(maxDeathPerTimeSlice[i-1], maxDeathPerTimeSlice[i-m] + x[i])
print(maxDeathPerTimeSlice[-1])
