
def u_and_l(string):
    upper = sum(1 for i in string if i.isupper())
    lower = sum(1 for j in string if j.islower())
    return upper,lower
s = "Hello my name is Altynai!"
print(u_and_l(s))