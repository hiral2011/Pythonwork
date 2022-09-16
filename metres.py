# class A:
#     def rk(self):
#         print(" In class A")
# class B(A):
#     def rk(self):
#         print(" In class B")
# class C(B):
#     def rk(self):
#         print("In class C")
 
# # classes ordering
# class C(B, C):
#     pass
    
# r = D()
# r.rk()


###############

class A:
    def rk(self):
        print(" In class A")
class B(A):
    def rk(self):
        print(" In class B")
class C(B):
    pass
class B(C):
    print(" In class D")

# class Parent:
#     print("hi")
# class Child(Parent):
#     print("hello")

# hiral = Child()


class E(D,C):
    pass
class F(E):
    print(" In class F")

r = F()
r.rk()

###############


 
class A:
    def rk(self):
        print(" In class A")
class B(A):
    def rk(self):
        print(" In class B")
class C(A):
    def rk(self):
        print("In class C")
 
classes ordering
class D(B, C):
    pass
    
r = D()
r.rk()