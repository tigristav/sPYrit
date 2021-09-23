
import dis, marshal

from code_parser import CodeParser

#magic number of 3.9.2 is 0x610d0d0a (found with deprecated method import importlib;importlib.util.MAGIC_NUMBER.hex()

MAGIC_NR = '610d0d0a'
HEADER_SIZE = 16
#OPCODE_MAP = dis.opmap
OPCODE_MAP = dict(zip(dis.opmap.values(), dis.opmap.keys())) #invert dict cause we lookup opcodes from their numerical value, not their name



class Decompiler:
    def __init__(self, path):
        self.file_content = self.decompile_file(path)
        self.OUTPUT_STRING = ''

    def decompile_file(self, path):
        with open(path, 'rb') as file:
            header = file.read(16)
            content = marshal.load(file)

        return content

    def reconstruct(self, content):
        print(dis.dis(content))
        self.OUTPUT_STRING = ((content.co_firstlineno-1) * '\n')

        parser = CodeParser(content, OPCODE_MAP)
        parser.line_tracker()
    #    parser.get_instruction_stack()
        print()
        self.OUTPUT_STRING += parser.get_output()

        with open('new.py', 'w') as file:
            file.write(self.OUTPUT_STRING)

    #    [print(e.__name__, end=', ') for e in self.INSTRUCTION_STACK]




if __name__ == '__main__':
    file_path = '__pycache__/main.cpython-39.pyc'
    dec = Decompiler(file_path)
    dec.reconstruct(dec.file_content)

