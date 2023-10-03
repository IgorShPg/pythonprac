def minus(n):
    return minus(n-1)+n**2 if n!=0 else 1
        


print(minus(eval(input())))



