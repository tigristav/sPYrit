
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
    if opcode.opcode.get(opc, None) is not None:
        opcode.opcode.get(opc, None)(argument)
    else:
        print(f'No opcode with the name {opc} exists in 3.9')



if __name__ == '__main__':
    file_return = decompile_file('__pycache__/main.cpython-39.pyc')
    reconstruct(file_return, Opcode(file_return, CODE_STACK, INSTRUCTION_STACK))
