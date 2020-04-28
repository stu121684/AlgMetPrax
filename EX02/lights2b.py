#Straßenlaternen

import sys
#Initialisierung/Einlesen_______________________________________________________________________
t=int(input()) #Testfälle
s=0
f=[0]*t
L=[0]*t
for s in range(0,t):
    b=sys.stdin.readline().split()  #l Länge, n Anzahl, r Radius
    a=[int(i) for i in b]
    p1=sys.stdin.readline().split()
    p2=[int(i) for i in p1]
    p=sorted(p2)
    l=a[0]
    n=a[1]
    r=a[2]
    h1=-1
#Programm________________________________________________________________________________________
    h=[0]*n
    k=0
    for j in range(0,n):
        for k in range(0,n):
            if j==0:
                if h[j] >= p[k]-r:
                    h1=p[k]
                elif h1<0:
                    f[s]=1
            elif h[j-1] >= p[k]-2*r:
                h1=p[k]
                #f[s]=0
            k=k+1
        h[j]=h1
        h1=-1
        if h[j]<0:
            f[s]=1
        j=j+1
    k=0
    q=0
    for k in range(0,n): #Welche Laterne beleuchtet gerade noch l?
        if l <= h[k]+r:
                q=q+1
        k=k+1
    if q==0:
        f[s]=1
        q=n-1
    else:
        q=n-(q-1)
    k=0
    p4=[0]*q
    for k in range(0,q):
        p4[k]=h[k]
    L[s]=len(p4)
    if s<t-1:
        c=input() #Zeilenumbruch
    s = s + 1
#Ausgabe_____________________________________________________________________
k=0
for k in range(0,t):
    if f[k]==1:
        print("Case #" +str(k+1)+ ": impossible")
    else:
        print("Case #"+str(k+1)+": "+str(L[k]))
    k=k+1
