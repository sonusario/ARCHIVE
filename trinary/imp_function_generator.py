from random import randrange
from time import time

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

def make_function():
    function_list = [F,U,T,imp,P,Q]

    function_string = "global new_function; new_function = lambda p,q: imp("
    function_string += implicator(function_list)
    function_string += ")"

    exec(function_string)
    return new_function, function_string

def implicator(fun_list):
    number_of_functions = len(fun_list)

    slot_1_selector = randrange(number_of_functions)
    slot_2_selector = randrange(number_of_functions)

    slot_1_function = fun_list[slot_1_selector]
    slot_2_function = fun_list[slot_2_selector]

    s1_string = quote(slot_1_function)
    s2_string = quote(slot_2_function)

    if s1_string == "imp":
        s1_string += "(" + implicator(fun_list) + ")"
    elif s1_string == 'P':
        s1_string = 'p'
    elif s1_string == 'Q':
        s1_string = 'q'

    if s2_string == "imp":
        s2_string += "(" + implicator(fun_list) + ")"
    elif s2_string == 'P':
        s2_string = 'p'
    elif s2_string == 'Q':
        s2_string = 'q'

    return s1_string + "," + s2_string

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

new_func,new_func_spec = make_function()

array_of_fun = [imp,new_func]
array_of_values = [F,U,T]

fun_test(array_of_fun, True)
print("\n" + "-"*80 +"\n")

def random_search(goal_string):
    print("Random search for '" + goal_string + "' started...")
    start_time = time()
    outp_string = ""
    while outp_string != goal_string:
        new_func,new_func_spec = make_function()
        outp_string = fun_test([new_func], False)
    print("Search completed in", time() - start_time, "seconds.")
    return new_func_spec
    

#orr_spec = random_search("FUTUUTTTT")

#nnd_spec = random_search("FFFFUUFUT")

#bic_spec = random_search("TUFUTUFUT")

add_spec = random_search("TFUFUTUTF")

#tand_spec = random_search("UTTTTTTTF")

#imp_spec = random_search("TTTUTTFUT")

#a_is_not_b_spec = random_search("FTTTFTTTF")
