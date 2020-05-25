#4A mit Dijkstra
from sys import stdin

def sol(l):
    b=[int(k) for k in range(l+m, n)]
    return b

def prio(M):
    i = 100
    liste1 = []
    liste2 = []
    for j in M:
        liste1.append(j)
        liste2.append(x[j])
    for j in liste1:
        if x[j] == max(liste2):
            i = j
    return i

t=stdin.readline().split()
n=int(t[0])
m=int(t[1])
y=stdin.readline().split()
x=[int(i) for i in y]
w=[int(i) for i in y]
x[0]=0
w[0]=0
L=[0]
Q=[]
while len(L)>0:
    i = prio(L)
    if i < 100:
        L.remove(i)
        Q.append(i)
    else:
        L = []
    for j in sol(i):
        if j not in Q:
            if (j not in L) or (j in L and x[i]+x[j] > x[j]):
                i = int(i)
                x[j] = x[i]+x[j]
                if j not in L:
                    L.append(j)
c = 0
d = 0
v = 0
for j in range(1, len(Q)-1):
    if Q[j]-Q[j-1] > 2:
        if v < 1:
            c = w[Q[j]]+w[Q[j-1]]
            v = v+1
        else:
            c = c+w[Q[j]]
        if d < c:
            d = c
    else:
        c = 0
        v = 0
print(d)



