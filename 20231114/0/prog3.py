def otv(tyty):
    def decor(fun):
        def newfun(*args):
            flag=True
            for i in args:
                if type(i)==tyty:
                    continue
                else:
                    flag=False
            if flag==True:
                return fun(*args)
            else:
                raise TypeError
        return newfun
    return decor

@otv(float)
def mult(a,b):
    return a*b

print(mult(4.2,"jfdjfdj"))
