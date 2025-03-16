def far_to_cen(farn):
    return (5 / 9) * (farn-32)

farn = float(input())
cent = far_to_cen(farn)
print(f"{farn}  Fahrenheit = {cent:.2f} C")