sum=0
a=eval(input())
sum+=a
while(sum<=21):
    if(a<=0):
        print(a)
        break
    a=eval(input())
    sum+=a
else:
    print(sum)
