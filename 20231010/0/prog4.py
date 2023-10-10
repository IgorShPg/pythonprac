from math import sin
def scale(a,b,A,B,x):
    return (x-a)*(B-A)/(b-a)+A



def output(scr):
    print("\n".join("".join(s) for s in scr))


W,H=60,20




scr=[[' ']*W for i in range(H)]
A,B=-5,5
for i in range(W):
    x=scale(0,W-1,A,B,i)
    y=sin(x)
    w=int(scale(-1,1,H-1,0,y))
    scr[w][i]="*"

output(scr)
