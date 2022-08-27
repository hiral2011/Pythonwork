
def add(a, b):
    sum = a + b
    return sum

def add2(a, b):
    sum = a + b
    return sum

def add3(a, b):
    sum = a + b
    return sum

def add4(a, b,c,d,e,f,g,h):
    sum = add(a,b)
    sum += add2(c,d)
    sum += add3(e,f)
    sum = sum+g+h
    return sum
sum = add4(1,2,3,4,5,6,7,8)
print(sum)