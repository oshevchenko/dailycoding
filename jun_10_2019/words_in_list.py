# This problem was asked by Microsoft.
# Given a dictionary of words and a string made up of those words (no spaces),
# return the original sentence in a list. If there is more than one possible
# reconstruction, return any of them. If there is no possible reconstruction,
# then return null.
# For example, given the set of words
# 'quick', 'brown', 'the', 'fox',
# and the string "thequickbrownfox",
# you should return ['the', 'quick', 'brown', 'fox'].
# Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond',
# and the string "bedbathandbeyond", return either
# ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].

set_of_words_1=['quick', 'brown', 'the', 'fox']
string_to_parse_1 = "thequickbrownfox"

set_of_words_2=['bed', 'bath', 'bedbath', 'beyond', 'and']
string_to_parse_2 = "bedbathandbeyond"

set_of_words_3=['bed', 'xxx', 'bedbath', 'bed', 'beyond', 'and']
string_to_parse_3 = "andbedbedbathandbeyond"


def recurse(G, set_of_words, string_to_parse, c_index, parent):
    for x in set_of_words:
        # print(x,c_index,string_to_parse)
        try:
            f_index = string_to_parse.index(x, c_index)
            if f_index == c_index:
                # print("FOUND!",x,c_index,string_to_parse)
                variant = (x, parent)
                new_c_index = c_index+len(x)
                if len(string_to_parse) > new_c_index:
                    recurse(G, set_of_words, string_to_parse, new_c_index, variant)
                else:
                    # print("append")
                    G.append(variant)

        except ValueError:
            # print("Haven't found:",x)
            new_set_of_words = []
            new_set_of_words.extend(set_of_words)
            new_set_of_words.remove(x)
            # variant = (x, parent)
            if len(new_set_of_words) != 0:
                recurse(G, new_set_of_words, string_to_parse, c_index, parent)

def main(set_of_words, string_to_parse):
    G = []
    recurse(G, set_of_words, string_to_parse, 0, None)
    # for k in G:
    #     print(k)
    found = False
    ret=[]
    for k in G:
        # print(k)
        ret=[]
        result_string = ''
        while len(k):
            word = k[0]
            ret.append(word)
            result_string = word+result_string
            if not k[1]:
                break
            else:
                k = k[1]
        # print(result_string)
        if result_string == string_to_parse:
            found = True
            ret.reverse()
            break
    if found:
        return ret
    else:
        return None


R = main(set_of_words_1, string_to_parse_1)
print(R)
R = main(set_of_words_2, string_to_parse_2)
print(R)
R = main(set_of_words_3, string_to_parse_3)
print(R)


