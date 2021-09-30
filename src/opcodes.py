
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
        self.CALL_FUNCTION_KW = self.call_function_kw
        self.RETURN_VALUE = self.return_value
        self.IMPORT_STAR = self.import_star
        self.IMPORT_NAME = self.import_name
        self.IMPORT_FROM = self.import_from
        self.BUILD_MAP = self.build_map
        self.BUILD_CONST_KEY_MAP = self.build_const_key_map
        self.DICT_UPDATE = self.dict_update
        self.STORE_SUBSCR = self.store_subscr
        self.BUILD_LIST = self.build_list
        self.LIST_EXTEND = self.list_extend
        self.BUILD_TUPLE = self.build_tuple
        self.LIST_TO_TUPLE = self.list_to_tuple
        self.BUILD_SET = self.build_set
        self.SET_UPDATE = self.set_update
        self.DUP_TOP = self.dup_top
        self.DUP_TOP_TWO = self.dup_top
        self.EXTENDED_ARG = self.extended_arg
        self.POP_TOP = self.pop_top
        self.NOP = self.nop
        self.ROT_TWO = self.rot_two
        self.ROT_THREE = self.rot_three
        self.ROT_FOUR = self.rot_four

        self.COMPARE_OP = self.compare_op
        self.IS_OP = self.is_op

        self.POP_JUMP_IF_TRUE = self.pop_jump_if_true
        self.POP_JUMP_IF_FALSE = self.pop_jump_if_false
        self.GET_ITER = self.get_iter
        self.FOR_ITER = self.for_iter
        self.JUMP_ABSOLUTE = self.jump_absolute
        self.JUMP_FORWARD = self.jump_forward

        self.LOAD_ATTR = self.load_attr
        self.LOAD_METHOD = self.load_method
        self.CALL_METHOD = self.call_method

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
        self.BINARY_MATRIX_MULTIPLY = self.binary_matrix_multiply
        self.INPLACE_SUBTRACT = self.inplace_subtract
        self.INPLACE_ADD = self.inplace_add
        self.INPLACE_TRUE_DIVIDE = self.inplace_true_divide
        self.INPLACE_FLOOR_DIVIDE = self.inplace_floor_divide
        self.INPLACE_POWER = self.inplace_power
        self.INPLACE_MULTIPLY = self.inplace_multiply
        self.INPLACE_MODULO = self.inplace_modulo
        self.INPLACE_LSHIFT = self.inplace_lshift
        self.INPLACE_RSHIFT = self.inplace_rshift
        self.INPLACE_AND = self.inplace_and
        self.INPLACE_XOR = self.inplace_xor
        self.INPLACE_OR = self.inplace_or
        self.INPLACE_MATRIX_MULTIPLY = self.inplace_matrix_multiply

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
            'CALL_FUNCTION_KW': self.CALL_FUNCTION_KW,
            'RETURN_VALUE': self.RETURN_VALUE,
            'IMPORT_STAR': self.IMPORT_STAR,
            'IMPORT_NAME': self.IMPORT_NAME,
            'IMPORT_FROM': self.IMPORT_FROM,
            'BUILD_MAP': self.BUILD_MAP,
            'BUILD_CONST_KEY_MAP': self.BUILD_CONST_KEY_MAP,
            'STORE_SUBSCR': self.STORE_SUBSCR,
            'DICT_UPDATE': self.DICT_UPDATE,
            'BUILD_LIST': self.BUILD_LIST,
            'LIST_EXTEND': self.LIST_EXTEND,
            'BUILD_TUPLE': self.BUILD_TUPLE,
            'LIST_TO_TUPLE': self.LIST_TO_TUPLE,
            'BUILD_SET': self.BUILD_SET,
            'SET_UPDATE': self.SET_UPDATE,
            'NOP': self.NOP,
            'POP_TOP': self.POP_TOP,
            'DUP_TOP': self.DUP_TOP,
            'DUP_TOP_TWO': self.DUP_TOP_TWO,
            'EXTENDED_ARG': self.EXTENDED_ARG,
            'ROT_TWO': self.rot_two,
            'ROT_THREE': self.rot_three,
            'ROT_FOUR': self.rot_four,

            'COMPARE_OP': self.COMPARE_OP,
            'IS_OP': self.IS_OP,

            'POP_JUMP_IF_TRUE': self.POP_JUMP_IF_TRUE,
            'POP_JUMP_IF_FALSE': self.POP_JUMP_IF_FALSE,
            'GET_ITER': self.GET_ITER,
            'FOR_ITER': self.FOR_ITER,
            'JUMP_ABSOLUTE': self.JUMP_ABSOLUTE,
            'JUMP_FORWARD': self.JUMP_FORWARD,

            'LOAD_ATTR': self.LOAD_ATTR,
            'LOAD_METHOD': self.LOAD_METHOD,
            'CALL_METHOD': self.CALL_METHOD,

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
            'BINARY_MATRIX_MULTIPLY': self.BINARY_MATRIX_MULTIPLY,
            'INPLACE_SUBTRACT': self.INPLACE_SUBTRACT,
            'INPLACE_ADD': self.INPLACE_ADD,
            'INPLACE_TRUE_DIVIDE': self.INPLACE_TRUE_DIVIDE,
            'INPLACE_FLOOR_DIVIDE': self.INPLACE_FLOOR_DIVIDE,
            'INPLACE_POWER': self.INPLACE_POWER,
            'INPLACE_MULTIPLY': self.INPLACE_MULTIPLY,
            'INPLACE_MODULO': self.INPLACE_MODULO,
            'INPLACE_LSHIFT': self.INPLACE_LSHIFT,
            'INPLACE_RSHIFT': self.INPLACE_RSHIFT,
            'INPLACE_AND': self.INPLACE_AND,
            'INPLACE_XOR': self.INPLACE_XOR,
            'INPLACE_OR': self.INPLACE_OR,
            'INPLACE_MATRIX_MULTIPLY': self.INPLACE_MATRIX_MULTIPLY,
        }
        return opc

    def update_func_args(self, names, count) -> None:
        # if we just send the names as arguments, argcount is redundant since
        # we can extract the required amount of names before calling this function
        # but mvp in the works so it will wait
        self.func_argcount = count
        self.func_argnames = list(names)

    def pop_top(self, arg) -> int:
        # fix later maybe idk
    #    self.code_stack.insert(0, self.indentation)
        self.instruction_stack.append(self.pop_top)
        return 0

    def nop(self, arg) -> None:
        self.instruction_stack.append(self.nop)
        pass

    def rot_two(self, arg) -> None:
        # print here
        self.code_stack[-1], self.code_stack[-2] = self.code_stack[-2], self.code_stack[-1]
        self.instruction_stack.append(self.rot_two)

    def rot_three(self, arg) -> None:
        # print here
        self.code_stack[-1], self.code_stack[-2], self.code_stack[-3] = self.code_stack[-2], self.code_stack[-3], self.code_stack[-1]
        self.instruction_stack.append(self.rot_three)

    def rot_four(self, arg) -> None:
        # print here
        self.code_stack[-1], self.code_stack[-2], self.code_stack[-3], self.code_stack[-4] = self.code_stack[-2], self.code_stack[-3], self.code_stack[-4], self.code_stack[-1]
        self.instruction_stack.append(self.rot_four)

    def load_const(self, arg) -> object:
        #print(f'LOAD_CONST {self.content.co_consts[arg]}')
        if isinstance(self.content.co_consts[arg], str):
            self.code_stack.append(f'\'{self.content.co_consts[arg]}\'')
        else:
            self.code_stack.append(self.content.co_consts[arg])
        self.instruction_stack.append(self.load_const)
        return self.content.co_consts[arg]

    def store_name(self, arg) -> None:
        # print(f'STORE_NAME {self.content.co_names[arg]}')
        if self.instruction_stack[-1] == self.make_function:
            self.code_stack.append('')
        elif self.instruction_stack[-1] == self.get_iter or self.instruction_stack[-1] == self.for_iter: # for loopie
            self.code_stack.append(f'for {self.content.co_names[arg]} in ')
        #    self.code_stack.append(f'{self.indentation}' + f'for {self.content.co_names[arg]} in ')
    #        self.indentation = self.indentation + (4 * ' ')
        elif self.instruction_stack[-1] in {self.INPLACE_MULTIPLY, self.INPLACE_ADD, self.INPLACE_SUBTRACT,
                                            self.INPLACE_ADD, self.INPLACE_TRUE_DIVIDE,self.INPLACE_FLOOR_DIVIDE,
                                            self.INPLACE_POWER, self.INPLACE_MULTIPLY, self.INPLACE_MODULO,
                                            self.INPLACE_LSHIFT, self.INPLACE_RSHIFT, self.INPLACE_AND,
                                            self.INPLACE_XOR, self.INPLACE_OR, self.INPLACE_MATRIX_MULTIPLY}:
            pass
        elif len(self.code_stack) > 0 and not isinstance(self.code_stack[-1], int) and self.code_stack[-1] is not None and 'from' in self.code_stack[-1]:
            self.code_stack.append(f' import {self.content.co_names[arg]}')
        else:
            self.code_stack.append(f'{self.indentation}' + f'{self.content.co_names[arg]} = ')

        self.instruction_stack.append(self.store_name)

    def load_name(self, arg) -> None:
        # print(f'LOAD_NAME {self.content.co_names[arg]}')
        self.code_stack.append(self.content.co_names[arg])
        self.instruction_stack.append(self.load_name)

    def load_global(self, arg) -> None:
        # print(f'LOAD_GLOBAL {self.content.co_names[arg]}')
        self.code_stack.append(self.content.co_names[arg])
        self.instruction_stack.append(self.load_global)

    def store_global(self, arg) -> None:
        # print(f'STORE_GLOBAL {self.content.co_names[arg]}')
        self.code_stack.append(f'{self.content.co_names[arg]} = ')
        self.instruction_stack.append(self.store_global)

    def store_fast(self, arg) -> None:
        # print(f'STORE_FAST {arg}')
    #    self.code_stack.append(f'{self.indentation}' + f'{self.content.co_varnames[arg]} = ')
        self.code_stack.append(f'{self.content.co_varnames[arg]} = ')
        self.instruction_stack.append(self.store_fast)

    def load_fast(self, arg) -> None:
        # print(f'LOAD_FAST {self.content.co_varnames[arg]}')
        self.code_stack.append(f'{self.content.co_varnames[arg]}')
        self.instruction_stack.append(self.load_fast)

    def make_function(self, arg) -> None:
        # print(f'MAKE_FUNCTION {arg}')
        function_name = self.code_stack.pop()
        code_obj = self.code_stack.pop()
        # print(f'code object?? {code_obj}')
        if '\'' in function_name:
            function_name = function_name[1:-1]
        if self.func_argcount > 0:
            if arg == 1:
                default_kw_values = self.code_stack.pop()
            else:
                default_kw_values = []
            args_list = []
            counter = 0
            for index in range(0, self.func_argcount):
                if 0 < len(default_kw_values) <= self.func_argcount-index and counter < len(default_kw_values):
                    if isinstance(default_kw_values[(len(default_kw_values)-1)-counter], str):
                        args_list.append(self.func_argnames.pop() + '=' + '\'' + str(default_kw_values[(len(default_kw_values)-1)-counter]) + '\'')
                    else:
                        args_list.append(self.func_argnames.pop() + '=' + str(default_kw_values[(len(default_kw_values)-1)-counter]))
                    counter += 1
                else:
                    args_list.append(self.func_argnames.pop())
            args_list.reverse() # can insert at 0 instead of this
            self.code_stack.append(f'def {function_name}({", ".join(args_list)}):')
        else:
            self.code_stack.append(f'def {function_name}({""}):')
        self.instruction_stack.append(self.make_function)

    def call_function(self, arg) -> None:
        # print(f'CALL_FUNCTION {self.code_stack[-(arg+1)]}')
        if self.instruction_stack[-1] != self.LIST_EXTEND:
            pos_arg = []
            for args in range(0, arg):
                pos_arg.insert(0, self.code_stack.pop())
            #    pos_arg.append(self.code_stack.pop())
            function_name = self.code_stack.pop()
            if all(isinstance(x, str) for x in pos_arg):
                self.code_stack.append(f'{function_name}({", ".join(pos_arg)})')
            else:
                str_content = ''
                for item in pos_arg:
                    # print(f'ITEM:{item} TYPE:{type(item)}')
                    str_content += f'{str(item)}, '
                str_content = str_content[:-2]
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

    def call_function_kw(self, arg) -> None:
        # print here
        arg_total = arg
        kw_names = self.code_stack.pop() # tuple elements must be strings
        kw_args = []
        for index in range(0, len(kw_names)):
            kw_args.append(kw_names[(len(kw_names)-1)-index] + '=' + str(self.code_stack.pop()))
        #    kw_args.append(kw_names[(len(kw_names)-1)-index] + '=' + str(self.code_stack.pop()))
        kw_args.reverse()
        pos_args = []
        for index in range(0, arg_total-len(kw_names)):
            pos_args.append(str(self.code_stack.pop()))
        pos_args.reverse()
        function_name = self.code_stack.pop()
        if len(pos_args) != 0:
            self.code_stack.append(f'{function_name}' + '(' + f'{", ".join(pos_args)}' + ', ' + f'{", ".join(kw_args)}' + ')')
        else:
            self.code_stack.append(f'{function_name}' + '(' + f'{", ".join(kw_args)}' + ')')
        self.instruction_stack.append(self.call_function_kw)

    def return_value(self, arg) -> None:
    #    print(f'RETURN_VALUE {self.code_stack[-1]}')
        return_value = self.code_stack.pop()
        print(return_value)
        if return_value is None:
            if len(self.indentation) != 0:
                self.code_stack.append(f'return {return_value}')
        #        self.code_stack.append(f'{self.indentation}' + f'return {return_value}')
            else:
                self.instruction_stack.append(self.return_value)
        else:
            self.code_stack.append(f'return {return_value}')
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
            for index in range(0, arg*2): #multiplied by 2 cause key value pair

                if index % 2 == 0:# and index != 0:
                    val = self.code_stack.pop()
                else:
                    key = self.code_stack.pop()
                    if key is not None and val is not None:
                        content.insert(0, str(key) + ':' + str(val))
            self.code_stack.append('{' + f'{", ".join(content)}' + '}')
        self.instruction_stack.append(self.build_map)

    def build_const_key_map(self, arg) -> None:
        #print(f'BUILD_CONST_KEY_MAP {arg}')
        key_tuple = self.code_stack.pop()
        values = []
        for index in range(0, arg):
            values.append(str(key_tuple[(arg-1)-index]) + ': ' + str(self.code_stack.pop()))
        values.reverse()
        self.code_stack.append('{' + f'{", ".join(values)}' + '}')
        self.instruction_stack.append(self.build_const_key_map)

    def dict_update(self, arg) -> None:
        pass

    def store_subscr(self, arg) -> None:
        # print here
        index = self.code_stack.pop()
        container = self.code_stack.pop()
        value = self.code_stack.pop()
        self.code_stack.append(f'{container}[{index}] = {value}')
        self.instruction_stack.append(self.store_subscr)

    def build_list(self, arg) -> None:
        # print(f'BUILD_LIST {arg}')
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
        # print(f'LIST_EXTEND {self.code_stack[-arg]}')
        if '[]' in self.code_stack:
            self.code_stack.reverse()
            self.code_stack.remove('[]')
            self.code_stack.reverse()
        contents = self.code_stack.pop()
        self.code_stack.append(list(contents))
        self.instruction_stack.append(self.list_extend)

    def build_tuple(self, arg) -> None:
        # print here
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
        # print here
        old_list = self.code_stack.pop()
        self.code_stack.append(tuple(old_list))
        self.instruction_stack.append(self.list_to_tuple)

    def build_set(self, arg) -> None:
        # print here
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
        self.instruction_stack.append(self.set_update)

    def dup_top(self, arg) -> None:
        # print here
        self.code_stack.append(self.code_stack[-1])
        self.instruction_stack.append(self.dup_top)

    def dup_top_two(self, arg) -> None:
        # print here
        # "Duplicates the two references on top of the stack, leaving them in the same order."
        # Assuming its the tos and tos1 but unclear what the docs mean since there can only be one on top of stack...
        self.code_stack.append(self.code_stack[-2])
        self.code_stack.append(self.code_stack[-1])
        self.instruction_stack.append()

    def extended_arg(self, arg) -> None:
        pass

    def compare_op(self, arg) -> None:
        # print here
        op = self.cmp_op[arg]
        right_side = self.code_stack.pop()
        left_side = self.code_stack.pop()
        self.code_stack.append(f'{left_side} {op} {right_side}')
        self.instruction_stack.append(self.compare_op)

    def is_op(self, arg) -> None:
        # print here
        right_side = self.code_stack.pop()
        left_side = self.code_stack.pop()
        if arg == 0:
            self.code_stack.append(f'{left_side} is {right_side}')
        else:
            self.code_stack.append(f'{left_side} is not {right_side}')
        self.instruction_stack.append(self.is_op)

    def pop_jump_if_true(self, arg) -> None:
        self.instruction_stack.append(self.pop_jump_if_true)
        pass

    def pop_jump_if_false(self, arg) -> None:
    #    self.indentation = self.indentation + (4 * ' ')
        self.instruction_stack.append(self.pop_jump_if_false)
        pass

    def get_iter(self, arg) -> None:
        if self.instruction_stack[-1] == self.call_function or self.instruction_stack[-1] == self.call_function_kw:
            func = self.code_stack.pop()
            func += ':'
            self.code_stack.append(func)
        self.instruction_stack.append(self.get_iter)

    def for_iter(self, arg) -> None:
        self.instruction_stack.append(self.for_iter)
        pass

    def jump_absolute(self, arg) -> None:
        print(f'stack')
        print(self.code_stack)
    #    self.indentation = self.indentation[:-4]
        self.instruction_stack.append(self.jump_absolute)
        pass

    def jump_forward(self, arg) -> None:
        self.instruction_stack.append(self.jump_forward)
        pass

    def load_attr(self, arg) -> None:
        # print here
        attr = self.content.co_names[arg]
        parent = self.code_stack.pop()
        self.code_stack.append(f'{parent}.{attr}')
        self.instruction_stack.append(self.load_attr)

    def load_method(self, arg) -> None:
        # print here
        name = self.content.co_names[arg]
        tos = self.code_stack.pop()
        self.code_stack.append(f'{tos}.{name}')
        self.instruction_stack.append(self.load_method)

    def call_method(self, arg) -> None:
        # print here
        arguments = []
        for _ in range(0, arg):
            arguments.append(self.code_stack.pop())
        arguments = [str(x) if x is None or isinstance(x, (int, float)) else '\'' + x + '\'' for x in arguments]
        method = self.code_stack.pop()
        self.code_stack.append(f'{method}' + '(' + f'{", ".join(reversed(arguments))}' + ')')
        self.instruction_stack.append(self.call_method)

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

    def binary_matrix_multiply(self, arg) -> None:
        # print here
        second_factor = self.code_stack.pop()
        first_factor = self.code_stack.pop()
        self.code_stack.append(f'{first_factor} @ {second_factor}')
        self.instruction_stack.append(self.binary_matrix_multiply)

    def inplace_subtract(self, arg) -> None:
        # print here
        second_term = self.code_stack.pop()
        first_term = self.code_stack.pop()
        self.code_stack.append(f'{first_term} *= {second_term}')
        self.instruction_stack.append(self.inplace_subtract)

    def inplace_add(self, arg) -> None:
        # print here
        second_term = self.code_stack.pop()
        first_term = self.code_stack.pop()
        self.code_stack.append(f'{first_term} += {second_term}')
        self.instruction_stack.append(self.inplace_add)

    def inplace_true_divide(self, arg) -> None:
        # print here
        divisor = self.code_stack.pop()
        dividend = self.code_stack.pop()
        self.code_stack.append(f'{dividend} /= {divisor}')
        self.instruction_stack.append(self.inplace_true_divide)

    def inplace_floor_divide(self, arg) -> None:
        # print here
        divisor = self.code_stack.pop()
        dividend = self.code_stack.pop()
        self.code_stack.append(f'{dividend} //= {divisor}')
        self.instruction_stack.append(self.inplace_floor_divide)

    def inplace_power(self, arg) -> None:
        # print here
        exponent = self.code_stack.pop()
        base = self.code_stack.pop()
        self.code_stack.append(f'{base} **= {exponent}')
        self.instruction_stack.append(self.inplace_power)

    def inplace_multiply(self, arg) -> None:
        # print here
        second_factor = self.code_stack.pop()
        first_factor = self.code_stack.pop()
        self.code_stack.append(f'{first_factor} *= {second_factor}')
        self.instruction_stack.append(self.inplace_multiply)

    def inplace_modulo(self, arg) -> None:
        # print here
        divisor = self.code_stack.pop()
        dividend = self.code_stack.pop()
        self.code_stack.append(f'{dividend} %= {divisor}')
        self.instruction_stack.append(self.inplace_modulo)

    def inplace_lshift(self, arg) -> None:
        # print here
        shift_value = self.code_stack.pop()
        base_value = self.code_stack.pop()
        self.code_stack.append(f'{base_value} <<= {shift_value}')
        self.instruction_stack.append(self.inplace_lshift)

    def inplace_rshift(self, arg) -> None:
        # print here
        shift_value = self.code_stack.pop()
        base_value = self.code_stack.pop()
        self.code_stack.append(f'{base_value} >>= {shift_value}')
        self.instruction_stack.append(self.inplace_rshift)

    def inplace_and(self, arg) -> None:
        # print here
        bits_2 = self.code_stack.pop()
        bits_1 = self.code_stack.pop()
        self.code_stack.append(f'{bits_1} &= {bits_2}')
        self.instruction_stack.append(self.inplace_and)

    def inplace_xor(self, arg) -> None:
        # print here
        bits_2 = self.code_stack.pop()
        bits_1 = self.code_stack.pop()
        self.code_stack.append(f'{bits_1} ^= {bits_2}')
        self.instruction_stack.append(self.inplace_xor)

    def inplace_or(self, arg) -> None:
        # print here
        bits_2 = self.code_stack.pop()
        bits_1 = self.code_stack.pop()
        self.code_stack.append(f'{bits_1} |= {bits_2}')
        self.instruction_stack.append(self.inplace_or)

    def inplace_matrix_multiply(self, arg) -> None:
        # print here
        second_factor = self.code_stack.pop()
        first_factor = self.code_stack.pop()
        self.code_stack.append(f'{first_factor} @= {second_factor}')
        self.instruction_stack.append(self.inplace_matrix_multiply)

