from sys import stdin

t = int(stdin.readline())
#main loop
for T in range(t):
    #parse input
    #vars as in problem statement
    rawInput = stdin.readline().split()
    l=int(rawInput[0])
    n=int(rawInput[1])
    r=int(rawInput[2])
    rawInput = stdin.readline().split()
    p = list(map(int,rawInput))
    p.sort()

    #we try to light every point on the line from 0 to incl. l
    #to light point 0 p must contain a position <=r. greedily the biggest such is the best
    #so we search for the j:=argmax{p_i<=r}
    #then we replace the start position 0 with the new start p_j+r
    #we go linearly through the array

    impossible = False
    start = 0
    lantern = 0
    counter = 0
    while (start<l and not impossible):
        #if there is no lantern to reach start from the left side
        if (lantern>=n or p[lantern]>start+r):
            impossible = True
        #while there could be a "better" lantern, more rightmost
        while (lantern<n and p[lantern]<=start+r):
            lantern+=1
        #the current lantern doesn't reach start anymore. the last one was the best
        counter+=1
        start = p[lantern-1]+r

    #print result of test case
    result = counter
    if impossible:
        result = "impossible"
    print("Case #{}: {}".format(T+1,result))

    #skip empty line
    if (not(T==t-1)):
        stdin.readline()
