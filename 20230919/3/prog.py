a=eval(input())
i=a
while(i<=a+2):
    j=a
    while(j<=a+2):
        n=i*j
        k=0
        while(n>0):
            k+=n%10
            n=n//10
        if(k==6):
            print(i,"*",j,"=",":=)",sep=' ',end=' ')
        else:  
            print(i,"*",j,"=",i*j,sep=' ',end=' ')
        j+=1
    print()
    i+=1
