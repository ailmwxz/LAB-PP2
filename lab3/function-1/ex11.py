def palindrom(uts):
    uts=uts.lower().replace(" ","")
    return uts==uts[::-1]
soz=input()
rep=soz[::-1]
print(soz, "its", rep)
print(palindrom(soz))
