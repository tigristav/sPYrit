
from opcodes import Opcode
import types


class CodeParser:
    def __init__(self, code_obj, opc_map, indentation=0):
        self.content = code_obj
        self.indentation = indentation
        self.CODE_STACK = []
        self.INSTRUCTION_STACK = []
        self.OUTPUT_STRING = ''
        self.RETURNED_STRING = ''
        self.function_lines = 0
        self.HAS_ARGUMENT = 90
        self.opcode = Opcode(self.content, self.CODE_STACK, self.INSTRUCTION_STACK, indentation)
        self.opcode_map = opc_map

    def line_tracker(self):
        start_line = 0
        counter = 0
        for num in self.content.co_lnotab:
            if counter % 2 == 0:
                self.byte_stepping(num, start_line)
                start_line += num
            else:
                print(f'{[x.__name__ for x in self.INSTRUCTION_STACK]}')
                if len(self.INSTRUCTION_STACK) > 1 and (self.INSTRUCTION_STACK[-2] is self.opcode.MAKE_FUNCTION or self.INSTRUCTION_STACK[-2].__name__ == 'make_function'):
                    modified_num = num - self.function_lines
                    self.OUTPUT_STRING += '\n'*modified_num
                else:
                    self.OUTPUT_STRING += '\n'*num

            counter += 1

        self.byte_stepping(len(self.content.co_code), start_line)

    def byte_stepping(self, num, line):
        start = line if line != 0 else 0
        end = start + num
        byte_slice = self.content.co_code[start:end]
        counter = 0
        for byte in byte_slice[0::2]:
            if byte >= self.HAS_ARGUMENT:
                self.match_opcode(byte, byte_slice[counter+1])
            else:
                self.match_opcode(byte, 0)

            counter += 2

        self.empty_stack_to_string()
        if self.RETURNED_STRING != '':                          #adding function body after declaration in output
            print(f'OLD OUTPUT: {self.OUTPUT_STRING}')
            self.OUTPUT_STRING += self.RETURNED_STRING
            self.function_lines = self.RETURNED_STRING.count('\n')
            self.RETURNED_STRING = ''
            print(f'NEW OUTPUT: {self.OUTPUT_STRING}')

    def match_opcode(self, instruction, argument):
        opc = self.opcode_map.get(instruction)
        if self.opcode.opcode.get(opc, None) is not None:
            result = self.opcode.opcode.get(opc, None)(argument)
            if isinstance(result, types.CodeType):
                parser = CodeParser(result, self.opcode_map, self.indentation+4)
                parser.line_tracker()
                self.RETURNED_STRING = parser.get_output()
                print(f'RETURNED {self.RETURNED_STRING}')
        else:
            print(f'No opcode with the name {opc} exists in 3.9')

    def empty_stack_to_string(self):
        while len(self.CODE_STACK) != 0:
            if self.CODE_STACK[-1] is not None:
                self.OUTPUT_STRING += str(self.CODE_STACK.pop())
            else:
                self.CODE_STACK.pop()

    def get_output(self):
        return self.OUTPUT_STRING

    def get_instruction_stack(self):
        [print(e.__name__, end=', ') for e in self.INSTRUCTION_STACK]
