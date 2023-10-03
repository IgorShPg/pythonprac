def summ(a,b):
    return lambda x:a(x)+b(x)

bobi=summ(bin,str)
print(bobi(123))
