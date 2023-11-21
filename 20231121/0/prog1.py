import sys

with open(sys.argv[1],"rb") as f:
    txt=f.read()

with open(sys.argv[1],"wb") as f:
    f.write(txt[len(txt)//2:])
    f.write(txt[:len(txt)//2])
