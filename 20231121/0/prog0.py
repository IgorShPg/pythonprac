f=open("test.txt","rb")

while b:=f.read(1):
    print(b,end=' ')

with open("test.txt","rb") as f:
    while b:=f.read(1):
        print(hex(b[0],end=' '))



