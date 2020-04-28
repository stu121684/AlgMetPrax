from sys import stdin

t = int(stdin.readline())

DELTA = 1e-7
for i in range(1, t+1):

    n,b = map(int, stdin.readline().split())

    val = list(map(int, stdin.readline().split()))
    low = 0
    high = 1
    while high - low > DELTA:
        mid = (low + high) / 2
        payoff = -b
        for index in range(n):
            payoff += pow(mid, index + 1) * val[index]
        if payoff <= 0:
            low = mid
        else:
            high = mid
    print("Case #{0}: {1:.6f}".format(i, low))

    # read empty line at the end of each sample
    try:
        stdin.readline()
    except EOFError:
        pass