from math import inf
import sys

def interpret(program):
    lines = program.strip().split("\n")
    commands = []
    labels = {}
    variables = {}
    while current_instruction < len(commands):
        line = commands[current_instruction]
        parts = line.split()
        if parts[0] == "stop":
            break
        elif parts[0] == "store":
            if len(parts) == 3:
                variables[parts[2]] = float(parts[1])
        elif parts[0] in ["add", "sub", "mul", "div"]:
            if len(parts) == 4:
                source = get_value(parts[1], variables)
                operand = get_value(parts[2], variables)
                destination = parts[3]
                if parts[0] == "add":
                    result = source + operand
                elif parts[0] == "sub":
                    result = source - operand
                elif parts[0] == "mul":
                    result = source * operand
                elif parts[0] == "div":
                    if operand != 0:
                        result = source / operand
                    else:
                        result = math.inf
                variables[destination] = result
        elif parts[0] in ["ifeq", "ifne", "ifgt", "ifge", "iflt", "ifle"]:
            if len(parts) == 4:
                source = get_value(parts[1], variables)
                operand = get_value(parts[2], variables)
                label = parts[3]
                if parts[0] == "ifeq" and source == operand:
                    current_instruction = labels.get(label, current_instruction+1)
                elif parts[0] == "ifne" and source != operand:
                    current_instruction = labels.get(label, current_instruction+1)
                elif parts[0] == "ifgt" and source > operand:
                    current_instruction = labels.get(label, current_instruction+1)
                elif parts[0] == "ifge" and source >= operand:
                    current_instruction = labels.get(label, current_instruction+1)
                elif parts[0] == "iflt" and source < operand:
                    current_instruction = labels.get(label, current_instruction+1)
                elif parts[0] == "ifle" and source <= operand:
                    current_instruction = labels.get(label, current_instruction+1)
        elif parts[0] == "out":
            if len(parts) == 2:
                source = get_value(parts[1], variables)
                print(source)
        
        current_instruction += 1



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
        case ['add' | 'sub' | 'mul' | 'div' as operation, *args]:
            perem[args[0]] = perem.setdefault(args[0], 0)
            perem[args[1]] = perem.setdefault(args[1], 0)
            perem[args[2]] = perem.setdefault(args[2], 0)
            match operation:
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


        case ['ifeq' | 'ifne' | 'ifgt' | 'ifge' | 'iflt' | 'ifle' as met,*args]:
            perem[args[0]] = perem.setdefault(args[0], 0)
            perem[args[1]] = perem.setdefault(args[1], 0)
            match met:
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

