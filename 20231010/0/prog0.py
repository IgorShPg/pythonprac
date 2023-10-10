import decimal
import fractions

def multiplier(x,y,Type):
    return Type(x)*Type(y)

print(multiplier(2/3,3/5,fractions.Fraction))
print(multiplier(2/3,3/5,decimal.Decimal))
print(multiplier(2/3,3/5,float))


