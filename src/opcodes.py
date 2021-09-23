
class Opcode:
    def __init__(self, content, code_stack, instruction_stack, indentation):
        self.content = content
        self.code_stack = code_stack
        self.instruction_stack = instruction_stack
        self.indentation = indentation * ' '
        self.func_argcount = 0
        self.func_argnames = []
        self.LOAD_CONST = self.load_const
        self.STORE_NAME = self.store_name
        self.LOAD_NAME = self.load_name
        self.LOAD_GLOBAL = self.load_global
        self.STORE_GLOBAL = self.store_global
        self.STORE_FAST = self.store_fast
        self.LOAD_FAST = self.load_fast
        self.MAKE_FUNCTION = self.make_function
        self.CALL_FUNCTION = self.call_function
        self.RETURN_VALUE = self.return_value
        self.IMPORT_STAR = self.import_star
        self.IMPORT_NAME = self.import_name
        self.IMPORT_FROM = self.import_from
        self.BUILD_MAP = self.build_map
        self.BUILD_CONST_KEY_MAP = self.build_const_key_map
        self.DICT_UPDATE = self.dict_update
        self.BUILD_LIST = self.build_list
        self.LIST_EXTEND = self.list_extend
        self.BUILD_TUPLE = self.build_tuple
        self.LIST_TO_TUPLE = self.list_to_tuple
        self.BUILD_SET = self.build_set
        self.SET_UPDATE = self.set_update
        self.DUP_TOP = self.dup_top

        self.COMPARE_OP = self.compare_op

        self.POP_JUMP_IF_TRUE = self.pop_jump_if_true
        self.POP_JUMP_IF_FALSE = self.pop_jump_if_false
        #build string

        self.BINARY_SUBTRACT = self.binary_subtract
        self.BINARY_ADD = self.binary_add
        self.BINARY_TRUE_DIVIDE = self.binary_true_divide
        self.BINARY_FLOOR_DIVIDE = self.binary_floor_divide
        self.BINARY_POWER = self.binary_power
        self.BINARY_MULTIPLY = self.binary_multiply
        self.BINARY_MODULO = self.binary_modulo
        self.BINARY_SUBSCR = self.binary_subscr
        self.BINARY_LSHIFT = self.binary_lshift
        self.BINARY_RSHIFT = self.binary_rshift
        self.BINARY_AND = self.binary_and
        self.BINARY_XOR = self.binary_xor
        self.BINARY_OR = self.binary_or

        # cmp_op valid for 3.9.2 (possibly changes based on version since it is originally in dis.cmp_op)
        self.cmp_op = ['<', '<=', '==', '!=', '>', '>=']
        self.opcode = self.get_opcodes()

    def get_opcodes(self) -> dict:
        opc = {
            'LOAD_CONST': self.LOAD_CONST,
            'STORE_NAME': self.STORE_NAME,
            'LOAD_NAME': self.LOAD_NAME,
            'LOAD_GLOBAL': self.LOAD_GLOBAL,
            'STORE_GLOBAL': self.STORE_GLOBAL,
            'STORE_FAST': self.STORE_FAST,
            'LOAD_FAST': self.LOAD_FAST,
            'MAKE_FUNCTION': self.MAKE_FUNCTION,
            'CALL_FUNCTION': self.CALL_FUNCTION,
            'RETURN_VALUE': self.RETURN_VALUE,
            'IMPORT_STAR': self.IMPORT_STAR,
            'IMPORT_NAME': self.IMPORT_NAME,
            'IMPORT_FROM': self.IMPORT_FROM,
            'BUILD_MAP': self.BUILD_MAP,
            'BUILD_CONST_KEY_MAP': self.BUILD_CONST_KEY_MAP,
            'BUILD_LIST': self.BUILD_LIST,
            'LIST_EXTEND': self.LIST_EXTEND,
            'BUILD_TUPLE': self.BUILD_TUPLE,
            'LIST_TO_TUPLE': self.LIST_TO_TUPLE,
            'BUILD_SET': self.BUILD_SET,
            'SET_UPDATE': self.SET_UPDATE,
            'POP_TOP': self.pop_top,
            'DUP_TOP': self.DUP_TOP,
            'COMPARE_OP': self.COMPARE_OP,
            'POP_JUMP_IF_TRUE': self.POP_JUMP_IF_TRUE,
            'POP_JUMP_IF_FALSE': self.POP_JUMP_IF_FALSE,
            'BINARY_SUBTRACT': self.BINARY_SUBTRACT,
            'BINARY_ADD': self.BINARY_ADD,
            'BINARY_TRUE_DIVIDE': self.BINARY_TRUE_DIVIDE,
            'BINARY_FLOOR_DIVIDE': self.BINARY_FLOOR_DIVIDE,
            'BINARY_POWER': self.BINARY_POWER,
            'BINARY_MULTIPLY': self.BINARY_MULTIPLY,
            'BINARY_MODULO': self.BINARY_MODULO,
            'BINARY_SUBSCR': self.BINARY_SUBSCR,
            'BINARY_LSHIFT': self.BINARY_LSHIFT,
            'BINARY_RSHIFT': self.BINARY_RSHIFT,
            'BINARY_AND': self.BINARY_AND,
            'BINARY_XOR': self.BINARY_XOR,
            'BINARY_OR': self.BINARY_OR,
        }
        return opc

    def update_func_args(self, names, count) -> None:
        #if we just send the names as arguments, argcount is redundant since
        #we can extract the required amount of names before calling this function
        #but mvp in the works so it will wait
        self.func_argcount = count
        self.func_argnames = list(names)

    def pop_top(self, arg):
        #fix later maybe idk
        return 0

    def load_const(self, arg) -> object:
        #print(f'LOAD_CONST {self.content.co_consts[arg]}')
        if isinstance(self.content.co_consts[arg], str):
            self.code_stack.append(f'\'{self.content.co_consts[arg]}\'')
        else:
            self.code_stack.append(self.content.co_consts[arg])
        self.instruction_stack.append(self.load_const)
        return self.content.co_consts[arg]

    def store_name(self, arg) -> None:
        #print(f'STORE_NAME {self.content.co_names[arg]}')
        if self.instruction_stack[-1] == self.make_function:
            self.code_stack.append('')
        elif len(self.code_stack) > 0 and not isinstance(self.code_stack[-1], int) and self.code_stack[-1] is not None and 'from' in self.code_stack[-1]:
            self.code_stack.append(f' import {self.content.co_names[arg]}')
        else:
            self.code_stack.append(f'{self.indentation}' + f'{self.content.co_names[arg]} = ')
        self.instruction_stack.append(self.store_name)

    def load_name(self, arg) -> None:
        #print(f'LOAD_NAME {self.content.co_names[arg]}')
        self.code_stack.append(self.content.co_names[arg])
        self.instruction_stack.append(self.load_name)

    def load_global(self, arg) -> None:
        #print(f'LOAD_GLOBAL {self.content.co_names[arg]}')
        self.code_stack.append(self.content.co_names[arg])
        self.instruction_stack.append(self.load_global)

    def store_global(self, arg) -> None:
        #print(f'STORE_GLOBAL {self.content.co_names[arg]}')
        self.code_stack.append(f'{self.content.co_names[arg]} = ')
        self.instruction_stack.append(self.store_global)

    def store_fast(self, arg) -> None:
        #print(f'STORE_FAST {arg}')
        self.code_stack.append(f'{self.indentation}' + f'{self.content.co_varnames[arg]} = ')
        self.instruction_stack.append(self.store_fast)

    def load_fast(self, arg) -> None:
        #print(f'LOAD_FAST {self.content.co_varnames[arg]}')
        self.code_stack.append(f'{self.content.co_varnames[arg]}')
        self.instruction_stack.append(self.load_fast)

    def make_function(self, arg) -> None:
        #print(f'MAKE_FUNCTION {arg}')
        function_name = self.code_stack.pop()
        code_obj = self.code_stack.pop()
        #print(f'code object?? {code_obj}')
        if '\'' in function_name:
            function_name = function_name[1:-1]
        if self.func_argcount > 0:
            temp = []
            for _ in range(0, self.func_argcount):
                temp.append(self.func_argnames.pop())
            temp.reverse() #can insert at 0 instead of this
            self.code_stack.append(f'def {function_name}({", ".join(temp)}):')
        else:
            self.code_stack.append(f'def {function_name}({""}):')
        self.instruction_stack.append(self.make_function)

    def call_function(self, arg) -> None:
        #print(f'CALL_FUNCTION {self.code_stack[-(arg+1)]}')
        if self.instruction_stack[-1] != self.LIST_EXTEND:
            pos_arg = []
            for args in range(0,arg):
                pos_arg.insert(0, self.code_stack.pop())
            #    pos_arg.append(self.code_stack.pop())
            function_name = self.code_stack.pop()
            if all(isinstance(x, str) for x in pos_arg):
                self.code_stack.append(f'{function_name}({", ".join(pos_arg)})')
            else:
                str_content = ''
                for item in pos_arg:
                    #print(f'ITEM:{item} TYPE:{type(item)}')
                    str_content += f', {str(item)}'
                self.code_stack.append(f'{function_name}({str_content})')
        else:
            pos_arg = self.code_stack.pop()
            function_name = self.code_stack.pop()
            if all(isinstance(x, str) for x in pos_arg):
                self.code_stack.append(f'{function_name}({", ".join(pos_arg)})')
            else:
                str_content = ''
                for item in pos_arg:
                    if isinstance(item, str):
                        str_content += f'\'{str(item)}\', '
                    else:
                        str_content += f'{str(item)}, '
                str_content = str_content[:len(str_content)-2]
                self.code_stack.append(f'{function_name}([{str_content}])')
        self.instruction_stack.append(self.call_function)

    def return_value(self, arg) -> None:
    #    print(f'RETURN_VALUE {self.code_stack[-1]}')
        return_value = self.code_stack.pop()
        if return_value is None:
            if self.indentation != 0:
                self.code_stack.append(f'{self.indentation}' + f'return {return_value}')
            else:
                self.instruction_stack.append(self.return_value)
        else:
            self.code_stack.append(f'{self.indentation}' + f'return {return_value}')
            self.instruction_stack.append(self.return_value)

    def import_star(self, arg) -> None:
        #print(f'IMPORT_STAR {self.code_stack[-arg]}')
        module_name = self.code_stack.pop()
        self.code_stack.append(f'from {module_name} import *')
        self.instruction_stack.append(self.import_star)

    def import_name(self, arg) -> None:
        #print(f'IMPORT_NAME {self.content.co_names[arg]}')
        fromlist = self.code_stack.pop()
        level = self.code_stack.pop()
        self.code_stack.append(f'from {self.content.co_names[arg]}')
        self.instruction_stack.append(self.import_name)

    def import_from(self, arg) -> None:
        #print(f'IMPORT_FROM {self.content.co_names[arg]}')
        self.instruction_stack.append(self.import_from)
        pass

    def build_map(self, arg) -> None:
        #print(f'BUILD_MAP {arg}')
        if arg == 0:
            self.code_stack.append('{}')
        else:
            content = []
            key = None
            val = None
            for index in range(0, arg):
                if index % 2 == 0:
                    content.insert(0, key+':'+val)
                    val = self.code_stack.pop()
                else:
                    key = self.code_stack.pop()
            self.code_stack.append('{' + f'{content}' + '}')
        self.instruction_stack.append(self.build_map)

    def build_const_key_map(self, arg) -> None:
        #print(f'BUILD_CONST_KEY_MAP {arg}')
        key_tuple = self.code_stack.pop()
        values = []
        for index in range(0, arg):
            values.append(key_tuple[index] + ':' + self.code_stack.pop())
        values.reverse()
        self.code_stack.append('{' + f'{values}' + '}')
        self.instruction_stack.append(self.build_const_key_map)

    def dict_update(self, arg) -> None:
        pass

    def build_list(self, arg) -> None:
        #print(f'BUILD_LIST {arg}')
        if arg == 0:
            self.code_stack.append('[]')
        else:
            elements = []
            for index in range(0, arg):
                if isinstance(self.code_stack[-1], str):
    #                elements.insert(0, "\'" + self.code_stack.pop() + "\'")
                    elements.insert(0, self.code_stack.pop())
                else:
                    elements.insert(0, self.code_stack.pop())
            #print(f'TYPE: {[x for x in elements]}')
            self.code_stack.append('[' + f'{", ".join(elements)}' + ']')
        self.instruction_stack.append(self.build_list)

    def list_extend(self, arg) -> None:
        #print(f'LIST_EXTEND {self.code_stack[-arg]}')
        if '[]' in self.code_stack:
            self.code_stack.reverse()
            self.code_stack.remove('[]')
            self.code_stack.reverse()
        contents = self.code_stack.pop()
        self.code_stack.append(list(contents))
        self.instruction_stack.append(self.list_extend)

    def build_tuple(self, arg) -> None:
        #print here
        if arg == 0:
            self.code_stack.append('()')
        else:
            elements = []
            for index in range(0, arg):
                if isinstance(self.code_stack[-1], str):
                    elements.insert(0, "\'" + self.code_stack.pop() + "\'")
                else:
                    elements.insert(0, self.code_stack.pop())
            if None in elements:
                elements = [str(x) if x is None else x[1:-1] for x in elements]
                self.code_stack.append('(' + f'{", ".join(elements)}' + ')')
            else:
                elements = [x[1:-1] for x in elements]
                self.code_stack.append('(' + f'{", ".join(elements)}' + ')')
        self.instruction_stack.append(self.build_tuple)

    def list_to_tuple(self, arg) -> None:
        #print here
        old_list = self.code_stack.pop()
        self.code_stack.append(tuple(old_list))
        self.instruction_stack.append(self.list_to_tuple)

    def build_set(self, arg) -> None:
        #print here
        if arg == 0:
            self.code_stack.append('{}')
        else:
            # is this really needed? will build_set ever be called with > 0 arg?
            # yes set constructor used this way will: set({'hello', 'there'})
            elements = []
            for index in range(0, arg):
                if isinstance(self.code_stack[-1], str):
                    elements.insert(0, "\'" + self.code_stack.pop() + "\'")
                else:
                    elements.insert(0, self.code_stack.pop())
            if None in elements:
                elements = [str(x) if x is None else x[1:-1] for x in elements]
                self.code_stack.append('{' + f'{", ".join(elements)}' + '}')
            else:
                elements = [x[1:-1] for x in elements]
                self.code_stack.append('{' + f'{", ".join(elements)}' + '}')
        self.instruction_stack.append(self.build_set)

    def set_update(self, args) -> None:
        # produces wrong order of elements in the set since a frozen set is applied on compilation which alters order
        if args > 0:
            # removes frozenset( and ) from constants since it is applied in 3.9 for whatever reason
            temp = list(self.code_stack.pop())
            empty_brackets = self.code_stack.pop() #remove the previous empty set brackets on stack
            temp = [str(x) if x is None or isinstance(x, (int, float)) else '\'' + x + '\'' for x in temp]
            self.code_stack.append('{' + f'{", ".join(temp)}' + '}')
            print(self.code_stack)
        self.instruction_stack.append(self.set_update)

    def dup_top(self, arg) -> None:
        #print here
        self.code_stack.append(self.code_stack[-1])
        self.instruction_stack.append(self.dup_top)

    def compare_op(self, arg) -> None:
        #print here
        op = self.cmp_op[arg]
        right_side = self.code_stack.pop()
        left_side = self.code_stack.pop()
        self.code_stack.append(f'{left_side} {op} {right_side}')
        self.instruction_stack.append(self.compare_op)

    def pop_jump_if_true(self, arg) -> None:
        pass

    def pop_jump_if_false(self, arg) -> None:
        pass

    def binary_subtract(self, arg) -> None:
        #print(f'BINARY_SUBTRACT {self.code_stack[-(arg-1)]} - {self.code_stack[-arg]}')
        second_term = self.code_stack.pop()
        first_term = self.code_stack.pop()
        self.code_stack.append(f'{first_term} - {second_term}')
        self.instruction_stack.append(self.binary_subtract)

    def binary_true_divide(self, arg) -> None:
        #print(f'BINARY_TRUE_DIVIDE {self.code_stack[-(arg-1)]} - {self.code_stack[-arg]}')
        divisor = self.code_stack.pop()
        dividend = self.code_stack.pop()
        self.code_stack.append(f'{dividend} / {divisor}')
        self.instruction_stack.append(self.binary_true_divide)

    def binary_floor_divide(self, arg) -> None:
        #print(f'BINARY_FLOOR_DIVIDE {self.code_stack[-(arg-1)]} // {self.code_stack[-arg]}')
        divisor = self.code_stack.pop()
        dividend = self.code_stack.pop()
        self.code_stack.append(f'{dividend} // {divisor}')
        self.instruction_stack.append(self.binary_floor_divide)

    def binary_add(self, arg) -> None:
        #print(f'BINARY_ADD {self.code_stack[-(arg-1)]} + {self.code_stack[-arg]}')
        second_term = self.code_stack.pop()
        first_term = self.code_stack.pop()
        self.code_stack.append(f'{first_term} + {second_term}')
        self.instruction_stack.append(self.binary_add)

    def binary_power(self, arg) -> None:
        #print(f'BINARY_POWER {self.code_stack[-(arg-1)]} ** {self.code_stack[-arg]}')
        exponent = self.code_stack.pop()
        base = self.code_stack.pop()
        self.code_stack.append(f'{base} ** {exponent}')
        self.instruction_stack.append(self.binary_power)

    def binary_multiply(self, arg) -> None:
        #print(f'BINARY_MULTIPLY {self.code_stack[-(arg-1)]} * {self.code_stack[-arg]}')
        second_factor = self.code_stack.pop()
        first_factor = self.code_stack.pop()
        self.code_stack.append(f'{first_factor} * {second_factor}')
        self.instruction_stack.append(self.binary_multiply)

    def binary_modulo(self, arg) -> None:
        #print(f'BINARY_MODULO {self.code_stack[-(arg-1)]} % {self.code_stack[-arg]}')
        divisor = self.code_stack.pop()
        dividend = self.code_stack.pop()
        self.code_stack.append(f'{dividend} % {divisor}')
        self.instruction_stack.append(self.binary_modulo)

    def binary_subscr(self, arg) -> None:
        #print(f'BINARY_SUBSCR {self.code_stack[-(arg-1)]}[{self.code_stack[-arg]}]')
        index = self.code_stack.pop()
        container = self.code_stack.pop()
        self.code_stack.append(f'{container}[{index}]')
        self.instruction_stack.append(self.binary_subscr)

    def binary_lshift(self, arg) -> None:
        #print(f'BINARY_LSHIFT {self.code_stack[-(arg-1)]} << {self.code_stack[-arg]}')
        shift_value = self.code_stack.pop()
        base_value = self.code_stack.pop()
        self.code_stack.append(f'{base_value} << {shift_value}')
        self.instruction_stack.append(self.binary_lshift)

    def binary_rshift(self, arg) -> None:
        #print(f'BINARY_RSHIFT {self.code_stack[-(arg-1)]} >> {self.code_stack[-arg]}')
        shift_value = self.code_stack.pop()
        base_value = self.code_stack.pop()
        self.code_stack.append(f'{base_value} >> {shift_value}')
        self.instruction_stack.append(self.binary_rshift)

    def binary_and(self, arg) -> None:
        #print(f'BINARY_AND {self.code_stack[-(arg-1)]} & {self.code_stack[-arg]}')
        bits_2 = self.code_stack.pop()
        bits_1 = self.code_stack.pop()
        self.code_stack.append(f'{bits_1} & {bits_2}')
        self.instruction_stack.append(self.binary_and)

    def binary_xor(self, arg) -> None:
        #print(f'BINARY_XOR {self.code_stack[-(arg-1)]} ^ {self.code_stack[-arg]}')
        bits_2 = self.code_stack.pop()
        bits_1 = self.code_stack.pop()
        self.code_stack.append(f'{bits_1} ^ {bits_2}')
        self.instruction_stack.append(self.binary_xor)

    def binary_or(self, arg) -> None:
        #print(f'BINARY_OR {self.code_stack[-(arg-1)]} | {self.code_stack[-arg]}')
        bits_2 = self.code_stack.pop()
        bits_1 = self.code_stack.pop()
        self.code_stack.append(f'{bits_1} | {bits_2}')
        self.instruction_stack.append(self.binary_or)

