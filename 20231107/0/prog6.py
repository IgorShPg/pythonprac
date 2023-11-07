a=eval(input())
for i in a:
    try:
        res=i[0]/i[1]
    except ZeroDivisionError:
        print("inf")
    else:
        print(res)
