import sys

with open(sys.argv[1],"rb") as f:
  txt=f.read()

W=len(txt)//3

p=txt[W-1:].find("\n")
print(txt[:W+p])
        
