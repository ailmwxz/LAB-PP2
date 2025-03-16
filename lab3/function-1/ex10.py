def unique_spisok(bir):
    unique=[]
    for num in bir:
        if num not in unique:
            unique.append(num)
    return unique

eki = list(input().split())
print( unique_spisok(eki))

