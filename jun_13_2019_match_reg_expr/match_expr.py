# This problem was asked by Facebook.

# Implement regular expression matching with the following
# special characters:

# . (period) which matches any single character
# * (asterisk) which matches zero or more of the preceding element
# That is, implement a function that takes in a string and a valid
# regular expression and returns whether or not the string matches
# the regular expression.

# For example, given the regular expression "ra." and the string
# "ray", your function should return true. The same regular
# expression on the string "raymond" should return false.

# Given the regular expression ".*at" and the string "chat", your
# function should return true. The same regular expression on the
# string "chats" should return false.

def recursive_ast(G, n_ast, n_char, parent):
    if not n_ast: return
    for i in range(n_char+1):
        variant=(i, parent)
        if n_ast==1:
            G.append(variant)
        else:
            recursive_ast(G, n_ast-1, n_char-i, variant)

def get_n_ast(reg_exp):
    n_ast = 0
    c_index = 0
    x='*'
    while True:
        try:
            ast_index = reg_exp.index(x, c_index)
            c_index = ast_index + 1
            n_ast = n_ast + 1
        except ValueError:
            break
    return n_ast

def extract_valid_variants(G, ast_chars):
    G_variants = []
    for i in G:
        variant = []
        while True:
            variant.append(i[0])
            i = i[1]
            if not i: break
        total = 0
        for j in variant:
            total = total + j
        if total == ast_chars:
            # print("valid variant", variant)
            G_variants.append(variant)
    return G_variants

def extend_reg_exp(G_reg_exp, G_variants, reg_exp):
    str_len = len(reg_exp)
    for i in G_variants:
        i_ast_in_variant = 0
        reg_exp_ext = ''
        for j in range(str_len):
            if reg_exp[j] == '*':
                for k in range(i[i_ast_in_variant]):
                    reg_exp_ext = reg_exp_ext + '.'
                i_ast_in_variant = i_ast_in_variant +1
            else:
                reg_exp_ext = reg_exp_ext + reg_exp[j]
        G_reg_exp.append(reg_exp_ext)
    # for reg_exp_var in G_reg_exp:
    #     print(reg_exp_var)
    return G_reg_exp

def final_match(G_reg_exp, input_string):
    str_len = len(input_string)
    match = False
    for reg_exp_var in G_reg_exp:
        # print(reg_exp_var)
        match = True
        for i in range(str_len):
            if reg_exp_var[i] == '.':
                continue
            elif reg_exp_var[i] != input_string[i]:
                match = False
                break
        if match: break
    return match



def match_expr(input_string, reg_exp):
    n_ast = get_n_ast(reg_exp)
    # print("n_ast",n_ast)
    G_reg_exp=[]
    if n_ast:
        G=[]
        ast_chars = len(input_string) - (len(reg_exp)-n_ast)
        # print("ast_chars",ast_chars)
        recursive_ast(G, n_ast, ast_chars, None)
        # if len(G):
        #     for i in G:
        #         print(i)

        G_variants = extract_valid_variants(G, ast_chars)
        G_reg_exp = extend_reg_exp(G_reg_exp, G_variants, reg_exp)
    else:
        if len(reg_exp) == len(input_string):
            G_reg_exp.append(reg_exp)
        else:
            return False
    match = final_match(G_reg_exp, input_string)
    # print("match", match)
    return match


print(match_expr("sdf0hello wo", "*.he*ll**"))
print(not match_expr("sdf0hello wo", ".he*ll*"))
print(match_expr("sdf0hello wo", "*.hell*"))
print(not match_expr("sdf0hello wo", "*.he*ll"))
print(not match_expr("sdf0hello wo", "*.hi*ll*"))
print(match_expr("ray", "ra."))
print(not match_expr("raymond", "ra."))
print(match_expr("chat", ".*at"))
print(not match_expr("chats", ".*at"))


