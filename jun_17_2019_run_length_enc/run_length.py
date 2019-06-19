# Run-length encoding is a fast and simple method
# of encoding strings. The basic idea is to represent
# repeated successive characters as a single count
# and character. For example, the string "AAAABBBCCDAA"
# would be encoded as "4A3B2C1D2A".

# Implement run-length encoding and decoding. You can
# assume the string to be encoded have no digits and
# consists solely of alphabetic characters. You can
# assume the string to be decoded is valid.

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

def create_string(s, string):
    G=[]
    if not len(string):
        return s
    string_l = list(string)
    encode(G, string_l)

    for (n, char) in G:
        s = s + str(n)
        s = s + char
        # print(s)
    return s

def main():
    string = "AAAABBBCCDAA"
    # string = "A"s
    # string = ""
    s = ""
    s = create_string(s, string)
    print(string)
    print(s)
    # for el in G:
    #     print(el)
main()


