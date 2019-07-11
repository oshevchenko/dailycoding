# [Hard]
# This problem was asked by Jane Street.
# Suppose you are given a table of currency
# exchange rates, represented as a 2D array.
# Determine whether there is a possible arbitrage:
# that is, whether there is some sequence of trades
# you can make, starting with some amount A of any
# currency, so that you can end up with some amount
# greater than A of that currency.
# There are no transaction costs and you can trade
# fractional quantities.

# UAH/USD 25.97  26.04
# UAH/EUR 29.15  29.32
# USD/EUR 1.121  1.126
E = [[1.000, 0.0384, 0.0341],
     [25.97, 1.0000, 0.8880],
     [29.15, 1.1210, 1.0000]]
def variant(seq, var, G):
    if len(seq) == 0:
        return

    for s in range(len(seq)):
        new_var = var.copy()
        new_seq = seq.copy()
        new_var.append(seq[s])
        del new_seq[s]
        # print(new_var)
        if len(new_var) > 1:
            new_var_full = new_var.copy()
            new_var_full.append(new_var_full[0])
            G.append(new_var_full)

        variant(new_seq, new_var, G)

def main():
    G = []
    seq = []
    var = []

    for i in range(len(E)):
        seq.append(i)

    variant(seq, var, G)
    print("0 - UAH, 1 - USD, 2 - EUR")
    print("Variant [(0, 1), (1, 2), (2, 0)] means:")
    print("exchange hryvna to USD, then USD to euro and finally euro to hryvna.")
    print("If total > 1.0 then arbitrage is possible.")
    # print(G)
    G_cells = []
    for k in G:
        cells = []
        for n in range(len(k)-1):
            cells.append((k[n],k[n+1]))
        G_cells.append(cells)
    for k in G_cells:
        total = 1.0
        for cell in k:
            # print(cell[0])
            total = total * E[cell[0]][cell[1]]
            # print(total)
        print("total: %.4f" % total, k)

main()

