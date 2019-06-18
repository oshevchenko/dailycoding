# This problem was asked by Palantir.

# Write an algorithm to justify text.
# Given a sequence of words and an integer line length k,
# return a list of strings which represents each line, fully justified.

# More specifically, you should have as many words
# as possible in each line. There should be at least
# one space between each word. Pad extra spaces when necessary
# so that each line has exactly length k. Spaces should be
# distributed as equally as possible, with the extra spaces,
# if any, distributed starting from the left.

# If you can only fit one word on a line, then you should
# pad the right-hand side with spaces.

# Each word is guaranteed not to be longer than k.

# For example, given the list of words
# ["the", "quick", "brown", "fox", "jumps", "over",
# "the", "lazy", "dog"]
# and k = 16, you should return the following:

# ["the  quick brown", # 1 extra space on the left
#  "fox  jumps  over", # 2 extra spaces distributed evenly
#  "the   lazy   dog"] # 4 extra spaces distributed evenly
def split_recursive(G, k, word_list):
    if not len(word_list): return
    total = 0
    sub_list = []
    total_len = 0
    while len(word_list):
        str_len = len(word_list[0])
        if total == 0:
            total += str_len
        else:
            total = total + 1 + str_len
        if total <= k:
            sub_list.append(word_list[0])
            total_len += str_len
            del(word_list[0])
        else:
            break
    element = (total_len, sub_list)
    G.append(element)
    split_recursive(G, k, word_list)

def spaces_per_gaps(s_per_g, n_spaces, n_gaps):
    if n_gaps == 0:
        s_per_g.append(n_spaces)
        return s_per_g
    s_per_g = [0] * n_gaps
    while True:
        for i in range(n_gaps):
            if n_spaces:
                s_per_g[i] += 1
                n_spaces -= 1
            else:
                return s_per_g

def create_string(string, s_per_g, sub_list):
    string += sub_list[0]
    spaces = ' ' * s_per_g[0]
    string += spaces
    n_sub_str = len(sub_list) - 1
    i = 1
    while n_sub_str:
        string += sub_list[i]
        n_sub_str -= 1
        if n_sub_str:
            spaces = ' ' * s_per_g[i]
            string += spaces
            i += 1
    # print(">",string,"<")
    return string

def create_strings(S, k, words):
    G = []
    split_recursive(G, k, words)
    for element in G:
        (total_len, sub_list) = element
        n_spaces = k - total_len
        n_gaps = len(sub_list) - 1
        s_per_g = []
        s_per_g = spaces_per_gaps(s_per_g, n_spaces, n_gaps)
        string = ''
        string = create_string(string, s_per_g, sub_list)
        S.append(string)
    return S


def main():
    k = 16
    words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
    # words = ["the", "quick", "brown", "fox", "jumps", "over", "the"]
    S = []
    S = create_strings(S, k, words)
    for s in S:
        print('>',s,'<')

main()