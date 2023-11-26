import sys
from functools import reduce
from operator import add

num=sys.stdin.buffer.read(1)
number=int(num[0])
text=sys.stdin.buffer.read()
L=len(text)
otv=num+reduce(add,sorted(text[i*L//number:(i+1)*L//number] for i in range(number)))
sys.stdout.buffer.write(otv)

