s=['A','-','B','-','C','-']
a=eval(input())
if (a%2==0) and (a%25==0):
    s[1]='+'
if (a%2==1) and (a%25==0):
    s[3]='+'
if (a%8==0):
    s[-1]='+'
print(*s,sep=' ', end = '')

