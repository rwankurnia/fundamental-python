word = "Today is Friday"

def tugasIlham(x):
    up = ""
    for i in x:
        if i not in ("aiueo"):
            up += i.upper() + i.lower()
        else:
            del(i)
    result = "".join(up)
    return result

mantapBroku = tugasIlham(word)
print(mantapBroku)