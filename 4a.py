from sys import stdin

def sol(l):
    b=[int(k) for k in range(l+m, n)]
    return b

t=stdin.readline().split()
n=int(t[0])
m=int(t[1])
y=stdin.readline().split()
x=[int(i) for i in y]
Q=[]
V=[0]*n
def cpm(i):
    Q.append(i)
    for j in sol(i):
        if j not in Q:
            cpm(j)
        if V[i]<x[j]+V[j]:
            V[i]=V[j]+x[j]
    return
cpm(0)
print(max(V))