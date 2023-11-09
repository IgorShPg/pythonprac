
class InvalidInput(Exception):pass


class BadTriangle(Exception):pass



def triangleSquare(inStr):
    try:
        (x1,y1), (x2,y2), (x3,y3)=eval(inStr)
    except Exception:
        raise InvalidInput
    for i in [x1,y1,x2,y2,x3,y3]:
        if not isinstance(i,int) and not isinstance(i,float):
            raise BadTriangle
    answer=abs((x2-x1)*(y3-y1)-(x3-x1)*(y2-y1))/2
    if answer<=0:
        raise BadTriangle
    return answer

while True:
    try:
        a=triangleSquare(input())
    except InvalidInput:
        print("Invalid input")
    except BadTriangle:
        print("Not a triangle")
    else:
        print(f"{a:.2f}")
        break
    
    
    
