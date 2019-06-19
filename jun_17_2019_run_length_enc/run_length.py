# Run-length encoding is a fast and simple method
# of encoding strings. The basic idea is to represent
# repeated successive characters as a single count
# and character. For example, the string "AAAABBBCCDAA"
# would be encoded as "4A3B2C1D2A".

# Implement run-length encoding and decoding. You can
# assume the string to be encoded have no digits and
# consists solely of alphabetic characters. You can
# assume the string to be decoded is valid.

from itertools import repeat

def encode(G, string):
    str_len = len(string)
    char = string[0]
    n = 1
    del(string[0])
    while True:
        if n == str_len:
            G.append((n, char))
            return
        if string[0] != char:
            break
        del(string[0])
        n += 1
    G.append((n, char))
    encode(G, string)

def decode(G, string):
    str_len = len(string)
    if not str_len: return
    s_num = ""
    while True:
        if not string[0].isdigit():
            break
        s_num += string[0]
        del(string[0])
    G.append((int(s_num), string[0]))
    del(string[0])
    decode(G, string)


def decode_string(s, string):
    G=[]
    if not len(string):
        return s
    string_l = list(string)
    decode(G, string_l)
    for (n, char) in G:
        s = s + "".join(list(repeat(char, n)))
        # print(s)
    return s

def encode_string(s, string):
    G=[]
    if not len(string):
        return s
    string_l = list(string)
    encode(G, string_l)
    for (n, char) in G:
        s += str(n)
        s += char
        # print(s)
    return s

def main():
    string = "AAAABBBCCDAA"
    # string = "A"
    # string = ""
    print(string)
    e_s = encode_string("", string)
    print(e_s)
    d_s = decode_string("", e_s)
    print(d_s)

main()


