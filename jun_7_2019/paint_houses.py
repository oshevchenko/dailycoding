
# This problem was asked by Facebook.

# A builder is looking to build a row of N houses that
# can be of K different colors. He has a goal of minimizing
# cost while ensuring that no two neighboring houses are
# of the same color.

# Given an N by K matrix where the nth row and kth column
# represents the cost to build the nth house with kth color,
# return the minimum cost which achieves this goal.

# R G B Y
# 1 2 3 4 < House 1
# 3 4 5 4 < House 2
# 3 4 5 4 < House 3
import numpy as np
N = 3
K = 4
G = []
G_valid = []
A = np.array([[1, 2, 3, 4], [3, 4, 5, 4], [3, 4, 5, 4]])

def variants(house, k, parent):
    # house = house-1
    if (house):
        for x in range(k):
            Z = np.zeros((1, k))
            Z[0,x] = 1
            variant = (Z, parent)
            # print(house, Z)
            variants(house-1, k, variant)
    else:
        G.append(parent)

def sortByPrice(val):
    return val[0]

# Z = np.zeros((1, K))
variants(N, K, None)
# print(len(G))
for x in range(len(G)):
    # print(">>>>>>>>>>>>>>>")
    variant = G[x]
    valid = True
    while True:
        check = variant[0]
        # print(variant[0])
        variant = variant[1]
        if variant == None:
            break
        else:
            total = np.add(check, variant[0])
            # print("total:",total)
            for y in range(total.size):
                if total[0,y] > 1:
                    valid = False
                    break
    # print("valid:", valid)
    if valid:
        G_valid.append(G[x])
G_price=[]
for x in range(len(G_valid)):
    variant = G_valid[x]
    total_variant_price = 0
    house = 0
    while True:
        check = variant[0]
        price = 0
        for y in range(check.size):
            house_price_list = A[house]
            # print("house_price_list:",house_price_list,"check",check)
            price = price + check[0, y]*house_price_list[y]
        total_variant_price = total_variant_price+price
        variant = variant[1]
        house = house+1
        if variant == None:
            break
    variant_price = (total_variant_price, G_valid[x])
    G_price.append(variant_price)


G_price.sort(key = sortByPrice)
print("RESULTS:")
print("Minimum price:",G_price[0][0])
print("total variants:",len(G_price))
print("Price list:")
print(A)
for variant_price in G_price:
    print("Price:",variant_price[0])
    print("Variant:")
    variant = variant_price[1]
    while True:
        print(variant[0])
        variant = variant[1]
        if variant == None:
            break
    print(">>>>>>>>>>>>>>>>>>>>")





