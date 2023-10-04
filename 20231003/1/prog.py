def pareto(*args):
    res=[]
    sravn=lambda x1,x2:(x1[0]<=x2[0] and x1[1]<=x2[1]) and (x1[0]<x2[0] or x1[1]<x2[1])
    for i in range(len(args)):
        help=True
        for j in range(len(args)):
            if i!=j and sravn(args[i],args[j]):
                help=False
                break
        if help:
            res.append(args[i])
    return tuple(res)
                
print(pareto(*eval(input())))
