s = "hello there !!how are you?"
a = [100,200,300]

def foo(arg):
    print(f'arg={arg}')

class foo:
    pass

############################

a = "hi hello"
b = "welcome to the team"
c = "hiral tarpara"
d = [1,2,3,4,5,6]



def aa():
    print(a)
# aa()
def bb():
    print(b)
# bb()
def cc():
    print(c)
# cc()
def dd():
    print(d)
# dd()

print(__name__)
if __name__ == '__main__':
    print(__name__=='__main__')
    aa()
    bb()
    cc()
    dd()
else:
    print("kdcuydzsucdzs")


#####################


def myFun(**kwargs):
	for key, value in kwargs.items():
		print("%s == %s" % (key, value))


# Driver code
myFun(first='Geeks', mid='for', last='Geeks')


