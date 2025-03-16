def ferm(numheads, numlegs):
    y = (numlegs - 2 * numheads) // 2
    x = numheads - y
    return x, y  
numheads = int(input())
numlegs = int(input())
chickens, rabbits = ferm(numheads, numlegs)
print(f"chicken: {chickens}, habbit: {rabbits}")
