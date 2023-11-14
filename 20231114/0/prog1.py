def deg(fun):
    def prov(*args):
        flag=True
        for i in args:
            if type(i)==int:
                continue
            else:
                flag=False
        if flag==True:
            return fun(*args)
        else:
            return TypeError
    return prov

@deg
def funny(a,b,c):
    return a*b*c

print(funny(1,3,3))
            
