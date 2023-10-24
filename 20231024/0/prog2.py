def genf():
    res=yield "START"
    while res:
        res=yield f"/{res}/"

ite=genf()
ite.send(123)
