while (s:=input()):
    n=int(s)
    if(n==13):
        break
    if(int(s)%2==0):
        print(s)
else:
    print("CONGRATS")
