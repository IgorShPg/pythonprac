from math import *

par=input().split()
w,h,a,b=int(par[0]),int(par[1]),int(par[2]),int(par[3])
func=lambda x:eval(par[4])
image=[[' ']*w for i in range(h)]
xv=[]
perem=a
while perem<b:
    xv.append(func(perem))
    perem+=(b-a)/w

minx,maxx=min(xv),max(xv)
scale=(h-1)/(maxx-minx)
xv=[(i-minx)*scale for i in xv]
xv=[h-1-int(i) for i in xv]

newx=[]
for i in range(1,w):
    if abs(xv[i-1]-xv[i])>1:
        for j in range(min(xv[i-1],xv[i]),max(xv[i-1],xv[i])):
            newx.append((i,j))
xv=[(i,xv[i]) for i in range(w)]+newx

for x,y in xv:
    image[y][x]="*"
for i in image:
    print("".join(i))
