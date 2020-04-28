from sys import stdin
n,m=stdin.readline().strip('\n').split(' ')
n = int(n)
m = int(m)
res = 0.0;
ls = []
for i in range(n):
    a,s,t=stdin.readline().strip('\n').split(' ')
    s = int(s)
    t = float(t)
    ls.append((s,t))
ls.sort(key=lambda x:-x[1])
i=0;
while m>0 and i<n:
    diff = min(m,ls[i][0])
    m=m-diff
    res+=diff*ls[i][1]
    i+=1
print(res)
