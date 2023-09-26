m,n=eval(input())
print([i for i in range(m,n) if not any([i%x==0 for x in range(2, i)])])
