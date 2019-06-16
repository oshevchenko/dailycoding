# This problem was asked by Facebook.

# Given a string of round, curly, and square open and closing brackets,
# return whether the brackets are balanced (well-formed).

# For example, given the string "([])[]({})", you should return true.

# Given the string "([)]" or "((()", you should return false.
def match_bracket(str, i, str_len):
    if str[i] == '(': bracket = ')'
    elif str[i] == '[': bracket = ']'
    elif str[i] == '{': bracket = '}'
    else:
        return -1

    while True:
        i += 1
        if i == str_len: return -1
        if str[i] == bracket:
            return i
        i = match_bracket(str, i, str_len)
        if i < 0: return -1

str_bracket0 = "([])[]{})()({})"
str_bracket1 = "([])[]({})()({})"
str_bracket2 = "([)]"
str_bracket3 = "(((("
str_bracket4 = ""
str_bracket5 = "("

def check_string(str):
    str_len = len(str)
    if str_len < 2: return False
    pos = 0
    while True:
        pos = match_bracket(str, pos, str_len)
        # print(pos)
        if pos < 0: return False
        pos += 1
        if pos == str_len: return True


print(not check_string(str_bracket0))
print(check_string(str_bracket1))
print(not check_string(str_bracket2))
print(not check_string(str_bracket3))
print(not check_string(str_bracket4))
print(not check_string(str_bracket5))
