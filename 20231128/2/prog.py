from math import inf
import sys
data = sys.stdin.read().split()
metka = {}
prov = []
text = []
perem = {}
count = 0

for i in range(len(data)):
    match data[i]:
        case 'store':
            res=data[i:i+3]
            text.append(' '.join(res))
            i += 2
        case 'add' | 'sub' | 'mul' | 'div':
            res=data[i:i+4]
            text.append(' '.join(res))
            i += 3
        case 'ifeq' | 'ifne' | 'ifgt' | 'ifge' | 'iflt' | 'ifle':
            res=data[i:i+4]
            prov.append(data[i+3])
            text.append(' '.join(res))
            i += 3
        case 'out':
            res=data[i:i+2]
            text.append(' '.join(res))
            i += 1
        case 'stop':
            text.append(data[i])
        case word:
            match word[-1]:
                case ':':
                    metka[data[i][:-1]] = len(text)
    i += 1

if  (len(prov) != len(set(prov))) or (len(metka.keys()) != len(set(metka.keys()))) or (set(prov) != set(metka.keys())):
    sys.exit()

while count < len(text):
    match text[count].split():
        case ['store', value, name]:
            perem[name] = float(value)
        case ['out', var]:
            perem[var] = perem.setdefault(var, 0)
            print(perem[var])
        case ['stop']:
            sys.exit()
        case ['add' | 'sub' | 'mul' | 'div' as OP, *args]:
            perem[args[0]] = perem.setdefault(args[0], 0)
            perem[args[1]] = perem.setdefault(args[1], 0)
            perem[args[2]] = perem.setdefault(args[2], 0)
            match OP:
                case 'add':
                    try:
                        perem[args[2]] = perem[args[0]] + perem[args[1]]
                    except Exception:
                        perem[args[2]] = inf
                case 'mul':
                    try:
                        perem[args[2]] = perem[args[0]] * perem[args[1]]
                    except Exception:
                        perem[args[2]] = inf
                case 'sub':
                    try:
                        perem[args[2]] = perem[args[0]] - perem[args[1]]
                    except Exception:
                        perem[args[2]] = inf
                case 'div':
                    try:
                        perem[args[2]] = perem[args[0]] / perem[args[1]]
                    except Exception:
                        perem[args[2]] = inf


        case ['ifeq' | 'ifne' | 'ifgt' | 'ifge' | 'iflt' | 'ifle' as CMP,*args]:
            perem[args[0]] = perem.setdefault(args[0], 0)
            perem[args[1]] = perem.setdefault(args[1], 0)
            match CMP:
                case 'ifeq':
                    if perem[args[0]] == perem[args[1]]:
                        count = metka[args[2]] - 1
                case 'ifne':
                    if perem[args[0]] != perem[args[1]]:                     
                        count = metka[args[2]] - 1
                case 'ifgt':
                    if perem[args[0]] > perem[args[1]]:                    
                        count = metka[args[2]] -1
                case 'ifge':
                    if perem[args[0]] >= perem[args[1]]:                
                        count = metka[args[2]] - 1
                case 'iflt':
                    if  perem[args[0]] < perem[args[1]]:
                        count = metka[args[2]] - 1
                case 'ifle':
                    if  perem[args[0]] <= perem[args[1]]:
                        count = metka[args[2]] - 1

    count +=1

