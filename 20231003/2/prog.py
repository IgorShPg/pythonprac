def mis(a,b):
    if(type(a) is list or type(a) is tuple) and (type(b) is list or type(b) is tuple):
        ans=[]
        for el in a:
            if el not in b:
                ans.append(el)
        return type(a)(ans)
    else:
        return a-b












print(mis(*eval(input())))
