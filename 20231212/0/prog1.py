from . import fun
import sys

print(fun(int(sys.argv[1]) if len(sys.args)>1 else 100500))
