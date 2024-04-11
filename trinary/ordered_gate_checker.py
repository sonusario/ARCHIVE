from random import randrange
from time import time
import re

debug_loop_counter = 0 # increment me somewhere

def quote(x):
    return x.__name__

def F(x, y, z):
    return x

def U(x, y, z):
    return y

def T(x, y, z):
    return z
#'''
def imp(p,q):
    return p(T, q(U,T,T), q)
'''
def imp(p,q):
    return p(q(U,T,T),T,q(T,T,F))
#'''
def P():
    return 'p'

def Q():
    return 'q'

function_list = [F,U,T,P,Q,imp]

val_code = {0:'F', 1:'U', 2:'T', 3:'P', 4:'Q', 5:'imp'}
rev_val_code = {'F':0,'U':1,'T':2,'P':3,'Q':4, 'imp':5}

base = 5

def int_to_val(arr):
    return ''.join(map(lambda x: val_code[x],arr))

def cycle(arr):
    d = len(arr) - 1
    while d >= 0:
        if arr[d] < base-1:
            arr[d] += 1
            return list(arr)
        else:
            arr[d] = 0
        d -= 1
    return list(arr)

def val_to_int(val_str):
    return list(map(lambda x: rev_val_code[x],list(val_str)))

def increment_input(prev):
    return int_to_val(cycle(val_to_int(prev)))

def input_cycler(in_length):
    val_str = 'F'*in_length

    combos = base ** in_length
    for i in range(combos + 1):
        print(str(i) + ':\t',val_str)
        val_str = increment_input(val_str)
    return

def increment_function_scaffold(prev):
    I_count = prev.count('I')
    last_I_index = prev.rfind('I')
    itr = 2
    while last_I_index != 0:
        prev_count = prev[last_I_index:].count('X')
        if prev_count > itr:
            return prev[0:last_I_index] + 'X' + 'I'*(itr-1) + 'X'*(prev_count-1)
        last_I_index = prev[0:last_I_index].rfind('I')
        itr += 1
    return 'I'*(I_count + 1) + 'X'*(I_count + 2)

def conv_char(char):
    if char == 'P':
        return 'p'
    elif char == 'Q':
        return 'q'
    return char

def sub_imp(function_code):
    if len(function_code) == 2:
        return conv_char(function_code[0]) + "," + conv_char(function_code[1])
    if function_code[0] == 'I':
        tail = function_code[-3:]
        if 'I' in tail:
            s1_string = "imp(" + sub_imp(function_code[1:-3]) + ")"
            s2_string = "imp(" + conv_char(tail[1]) + "," + conv_char(tail[2]) + ")"
        else:
            s1_string = "imp(" + sub_imp(function_code[1:-1]) + ")"
            s2_string = conv_char(function_code[-1])
    else:
        s1_string = conv_char(function_code[0])
        s2_string = "imp(" + sub_imp(function_code[2:]) + ")"
    return s1_string + "," + s2_string

def implicator(function_code):
    function_string = "imp("
    f_string_addition= sub_imp(function_code[1:])
    function_string += f_string_addition
    function_string += ")"
    return function_string

def make_function(scaff_code,input_code):
    function_code = ""
    for c in scaff_code:
        if c == 'X':
            function_code += input_code[0]
            input_code = input_code[1:]
        else:
            function_code += 'I'
    function_string = "global new_function; new_function = lambda p,q: "
    function_string += implicator(function_code)

    exec(function_string)
    return new_function, function_code

def fun_test(array_of_fun, print_flag):
    output_string = ""
    for func in array_of_fun:
        if print_flag:
            print('\n')
            print("a b |", quote(func))
            print("=========")
        for val_a in array_of_values:
            for val_b in array_of_values:
                if print_flag:
                    print(quote(val_a), quote(val_b),
                          "| ", quote(func(val_a,val_b)))
                output_string += quote(func(val_a,val_b))
    if print_flag:
        print("\n")
    return output_string

def ordered_search(goal_string):
    global debug_loop_counter
    debug_loop_counter = 0
    print("Ordered search for '" + goal_string + "' started...")
    start_time = time()
    outp_string = ""
    scaff_code = "IIIIIXXXXXX"
    input_code = "F" * scaff_code.count("X")
    check_rep = input_code
    while outp_string != goal_string:
        new_func,new_func_spec = make_function(scaff_code,input_code)
        outp_string = fun_test([new_func], False)
        input_code = increment_input(input_code)
        debug_loop_counter += 1
        if input_code == check_rep:
            input_code += "F"
            check_rep = input_code
            scaff_code = increment_function_scaffold(scaff_code)
            print("Current spec after", time()-start_time, "seconds:", new_func_spec)
            print("Core loop count:", debug_loop_counter)
            print()
    print("Search completed in", time() - start_time, "seconds.")
    return new_func_spec

new_func,new_func_spec = make_function("IXX","FF")

array_of_fun = [imp,new_func]
array_of_values = [F,U,T]

fun_test(array_of_fun, True)
print("\n" + "-"*80 +"\n")

not_spec = ordered_search("TTTUUUFFF")

orr_spec = ordered_search("FUTUUTTTT")

nnd_spec = ordered_search("FFFFUUFUT")

imp_spec = ordered_search("TTTUTTFUT")

bic_spec = ordered_search("TUFUTUFUT")

tand_spec = ordered_search("UTTTTTTTF")

a_is_not_b_spec = ordered_search("FTTTFTTTF")
