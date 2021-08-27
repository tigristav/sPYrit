
import dis, marshal
import types
from opcodes import Opcode

#magic number of 3.9.2 is 0x610d0d0a (found with deprecated method import importlib;importlib.util.MAGIC_NUMBER.hex()

MAGIC_NR = '610d0d0a'
HEADER_SIZE = 16
#OPCODE_MAP = dis.opmap
OPCODE_MAP = dict(zip(dis.opmap.values(), dis.opmap.keys())) #invert dict cause we lookup opcodes from their numerical value, not their name
HAS_ARGUMENT = 90

FILE_STRING = ''

CODE_STACK = []
INSTRUCTION_STACK = []


def decompile_file(path):
    with open(path, 'rb') as file:
        header = file.read(16)
        content = marshal.load(file)

    return content


def reconstruct(content, opcode):
    #with open('new.py', 'w') as file:
    print(dis.dis(content))

    global FILE_STRING
    FILE_STRING = ((content.co_firstlineno-1) * '\n') #+ str(content.co_firstlineno)
    #print(FILE_STRING)

    print(content.co_lnotab.hex())
    #for b in content.co_code[:8]:
    #    print(b, end=' ')
    print()
    #print(content.co_code[:content.co_lnotab[0]])

    automation(content, opcode)

    with open('new.py', 'w') as file:
        file.write(FILE_STRING)

    [print(e.__name__, end=', ') for e in INSTRUCTION_STACK]


def automation(content, opcode):
    global FILE_STRING
    start_tracker = 0
    counter = 0
    for num in content.co_lnotab:
 #       print(f'{num+start_tracker} {start_tracker+start_tracker}')
        if counter % 2 == 0:
            byte_stepping(num, start_tracker, content, opcode)
            start_tracker += num
        else:
            FILE_STRING += '\n'*num

        counter += 1

    byte_stepping(len(content.co_code), start_tracker, content, opcode)


def byte_stepping(num, start_tracker, content, opcode):
    start = start_tracker if start_tracker != 0 else 0
    end = start + num
    print(f'{start} {end}')
    byte_slice = content.co_code[start:end]
    print(byte_slice)
    counter = 0
    for byte in byte_slice[0::2]:
        if byte >= HAS_ARGUMENT:
            match_opcode(byte, byte_slice[counter+1], opcode)
        else:
            match_opcode(byte, 0, opcode)

        counter += 2

    global FILE_STRING
    global CODE_STACK
    print(CODE_STACK)
    while len(CODE_STACK) != 0:
        if not isinstance(CODE_STACK[-1], types.CodeType): #remove codetype check after proper implementation of code objects
            if CODE_STACK[-1] is not None and 'import' in CODE_STACK[-1]:
                FILE_STRING += str(CODE_STACK.pop(len(CODE_STACK)-2))
            elif CODE_STACK[-1] is not None:
                if '=' in CODE_STACK[-1] and len(CODE_STACK) > 1:
                    FILE_STRING += str(CODE_STACK.pop()) + str(CODE_STACK.pop())
                else:
                    FILE_STRING += str(CODE_STACK.pop())
            else:
                CODE_STACK.pop()
        #    INSTRUCTION_STACK.pop() #hmmm
        else:
            CODE_STACK.pop()


def match_opcode(instruction, argument, opcode):
    opc = OPCODE_MAP.get(instruction)
    if opc == 'LOAD_CONST':
        opcode.LOAD_CONST(argument)
    elif opc == 'STORE_NAME':
        opcode.STORE_NAME(argument)
    elif opc == 'LOAD_NAME':
        opcode.LOAD_NAME(argument)
    elif opc == 'LOAD_GLOBAL':
        opcode.LOAD_GLOBAL(argument)
    elif opc == 'STORE_GLOBAL':
        opcode.STORE_GLOBAL(argument)
    elif opc == 'CALL_FUNCTION':
        opcode.CALL_FUNCTION(argument)
    elif opc == 'IMPORT_STAR':
        opcode.IMPORT_STAR(argument)
    elif opc == 'IMPORT_NAME':
        opcode.IMPORT_NAME(argument)
    elif opc == 'IMPORT_FROM':
        opcode.IMPORT_FROM(argument)
    elif opc == 'BUILD_MAP':
        opcode.BUILD_MAP(argument)
    elif opc == 'BUILD_CONST_KEY_MAP':
        opcode.BUILD_CONST_KEY_MAP(argument)
    elif opc == 'BUILD_LIST':
        opcode.BUILD_LIST(argument)
    elif opc == 'LIST_EXTEND':
        opcode.LIST_EXTEND(argument)

    elif opc == 'POP_TOP':
        print('hehe')
        pass
    elif opc == 'BINARY_SUBTRACT':
        opcode.BINARY_SUBTRACT(argument)
    elif opc == 'BINARY_ADD':
        opcode.BINARY_ADD(argument)
    elif opc == 'BINARY_TRUE_DIVIDE':
        opcode.BINARY_TRUE_DIVIDE(argument)
    elif opc == 'BINARY_FLOOR_DIVIDE':
        opcode.BINARY_FLOOR_DIVIDE(argument)
    elif opc == 'BINARY_POWER':
        opcode.BINARY_POWER(argument)
    elif opc == 'BINARY_MULTIPLY':
        opcode.BINARY_MULTIPLY(argument)
    elif opc == 'BINARY_MODULO':
        opcode.BINARY_MODULO(argument)
    elif opc == 'BINARY_SUBSCR':
        opcode.BINARY_SUBSCR(argument)
    elif opc == 'BINARY_LSHIFT':
        opcode.BINARY_LSHIFT(argument)
    elif opc == 'BINARY_RSHIFT':
        opcode.BINARY_RSHIFT(argument)
    elif opc == 'BINARY_AND':
        opcode.BINARY_AND(argument)
    elif opc == 'BINARY_XOR':
        opcode.BINARY_XOR(argument)
    elif opc == 'BINARY_OR':
        opcode.BINARY_OR(argument)

    #print(f'{instruction} {argument}')
    #pass


file_return = decompile_file('__pycache__/main.cpython-39.pyc')
reconstruct(file_return, Opcode(file_return, CODE_STACK, INSTRUCTION_STACK))
