def grams_to_ounces(grams):
    return grams * 28.3495231

grams = float(input())
ounces = grams_to_ounces(grams)
print(f"{grams} grams = {ounces:.2f} ounces")