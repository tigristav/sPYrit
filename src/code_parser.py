
from opcodes import Opcode
import types

# NOTE to self: when comparing something with INSTRUCTION_STACK content, == not is

class CodeParser:
    def __init__(self, code_obj, opc_map, indentation=0):
        self.content = code_obj
        self.indentation = indentation
        self.CODE_STACK = []
        self.INSTRUCTION_STACK = []
        self.MASTER_STACK = []
        self.OUTPUT_STRING = ''
        self.RETURNED_STRING = ''
        self.RETURNED_ARGS = []
        self.function_lines = 0
        self.statement_indent = 0
        self.multiple_line_func = 0
        self.HAS_ARGUMENT = 90
        self.opcode = Opcode(self.content, self.CODE_STACK, self.INSTRUCTION_STACK, indentation)
        self.opcode_map = opc_map

    def line_tracker(self):
        start_line = 0
        counter = 0
        for num in self.content.co_lnotab:
            if num > 127:   # line overflow fix
                num = 127-num
            if counter % 2 == 0:
                self.byte_stepping(num, start_line, False)
                start_line += num
            else:
    #            print(f'{[x.__name__ for x in self.INSTRUCTION_STACK]}')
                if len(self.MASTER_STACK) > 1 and (self.MASTER_STACK[-2] is self.opcode.MAKE_FUNCTION or self.MASTER_STACK[-2].__name__ == 'make_function'):
                    modified_num = num - self.function_lines
                    self.OUTPUT_STRING += '\n'*modified_num
                else:
                    if self.multiple_line_func != 0:
                        self.OUTPUT_STRING = self.OUTPUT_STRING[:-self.multiple_line_func]
                        self.multiple_line_func = 0
                    self.OUTPUT_STRING += '\n'*num

            counter += 1

        self.byte_stepping(len(self.content.co_code), start_line, True)

    def byte_stepping(self, num, line, is_end):
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
    #    if is_end and self.indentation == 0:
    #        print(f'last pop', self.CODE_STACK.pop())

    #    if is_end and self.INSTRUCTION_STACK[-2] == self.opcode.for_iter:
    #        self.indentation += 4
    #        self.opcode.indentation = self.opcode.indentation + (self.indentation * ' ')
        self.empty_stack_to_string()

    #    print(f'output: {self.OUTPUT_STRING}')
    #    if self.OUTPUT_STRING.isspace():
    #        self.OUTPUT_STRING.strip(' ')
    #    print(f'output: {self.OUTPUT_STRING}')

        if self.RETURNED_STRING != '':                          #adding function body after declaration in output
        #    print(f'OLD OUTPUT: {self.OUTPUT_STRING}')

            self.OUTPUT_STRING += self.RETURNED_STRING
            self.function_lines = self.RETURNED_STRING.count('\n')
            self.RETURNED_STRING = ''
        #    print(f'NEW OUTPUT: {self.OUTPUT_STRING}')

    def match_opcode(self, instruction, argument):
        opc = self.opcode_map.get(instruction)
        if self.opcode.opcode.get(opc, None) is not None:
        #    print(f'{opc} {argument}')
            if self.opcode.opcode.get(opc, None) is self.opcode.opcode.get('MAKE_FUNCTION') and \
                    len(self.RETURNED_ARGS) > 0:
                self.opcode.update_func_args(self.RETURNED_ARGS.pop(), self.RETURNED_ARGS.pop())
            result = self.opcode.opcode.get(opc, None)(argument)
            if isinstance(result, types.CodeType):
                self.RETURNED_ARGS.append(result.co_argcount)
                self.RETURNED_ARGS.append(result.co_varnames[:result.co_argcount])
                parser = CodeParser(result, self.opcode_map, self.indentation+4)
                parser.line_tracker()
                self.RETURNED_STRING = parser.get_output()
        else:
            print(f'No opcode with the name {opc} exists in 3.9')

    def empty_stack_to_string(self):
        #if len(self.INSTRUCTION_STACK) > 4:
        #    if self.INSTRUCTION_STACK[-1] is not self.opcode.opcode.get('MAKE_FUNCTION', None) and \
        #            self.INSTRUCTION_STACK[-3] is not self.opcode.opcode.get('MAKE_FUNCTION', None) \
        #            and self.INSTRUCTION_STACK[-4] is not self.opcode.opcode.get('MAKE_FUNCTION', None):
        self.OUTPUT_STRING += self.indentation * ' '
        self.OUTPUT_STRING += self.statement_indent * ' '
        while len(self.CODE_STACK) != 0:
            if self.CODE_STACK[-1] is not None:
                self.OUTPUT_STRING += str(self.CODE_STACK.pop())
            else:
                self.OUTPUT_STRING += str(self.CODE_STACK.pop())
        #        self.CODE_STACK.pop()
        if self.OUTPUT_STRING[-3:].isspace():
            self.OUTPUT_STRING = self.OUTPUT_STRING[0:len(self.OUTPUT_STRING)-4]

        if self.opcode.opcode.get("FOR_ITER") in self.INSTRUCTION_STACK or \
                (self.opcode.opcode.get("POP_JUMP_IF_FALSE") in self.INSTRUCTION_STACK and self.opcode.opcode.get("COMPARE_OP") in self.INSTRUCTION_STACK) or \
                (self.opcode.opcode.get("POP_JUMP_IF_TRUE") in self.INSTRUCTION_STACK and self.opcode.opcode.get("COMPARE_OP") in self.INSTRUCTION_STACK):
            self.statement_indent += 4
        elif self.opcode.opcode.get("JUMP_ABSOLUTE") in self.INSTRUCTION_STACK:
            self.statement_indent -= 4
            if self.statement_indent < 0:
                self.statement_indent = 0
        self.MASTER_STACK.extend(self.INSTRUCTION_STACK)
        self.INSTRUCTION_STACK.clear()

    def get_output(self):
        return self.OUTPUT_STRING

    def get_instruction_stack(self):
        [print(e.__name__, end=', ') for e in self.INSTRUCTION_STACK]
