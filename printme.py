from locale import strcoll
# from fib import fib////////////////


# def printme( str ):
#     print(str)
#     return

# printme()

# def changeme( mylist ):
#    print (mylist)
   
#    mylist[2]=50
#    print (mylist)
#    return

# # Now you can call changeme function
# mylist = [30,40,70]
# changeme( mylist )
# print ("Values outside the function: ", mylist)

# def changeme2(mylist):
#     print(mylist)
#     mylist[4]=20
#     print(mylist)
#     return
# mylist=[1,2,3,4,5,6,7,8]
# changeme2(mylist)


# def abc():
#     # mylist=[1,2,3,4,5]
#     print("hello")
#     return
# abc()


# def printme( str ):
#     print (str)
#     return
# printme("My string")

# def info(name,age,std):
#     print("name=",name)
#     print("age=",age)
#     print("std=",std)
#     return
# info("hiral",23,"bsc")

# def info(name,age=35):
#     print(name)
#     print(age)
#     return
# info("hiral",age=50)

# def abc():
#     mylist=[1,2,3,4,5]
#     print(mylist)
#     return
# abc()

# def abc(mylist):
#     mylist=[1,2,3,4,5]
#     print(mylist)
#     return
# mylist=[6,7,89,0]
# abc(mylist)
# print(mylist)

# def printinfo( arg1, *vartuple ):
#    print ("Output is: ")
#    print ()
#    for var in vartuple:
#       print (var)
#    return
# # printinfo( 10 )
# printinfo( 70, 60, 50,20,10,30 )

# sum = lambda a,b,c:a+b+c
# print("sum=",sum(1,2,3))





# def sum(a,b):
#     total=a+b
#     print(total)
#     return total
# total=sum(20,40)
# print(total)

# total = 0   # This is global variable.
# def sum( arg1, arg2 ):
#    total = arg1 + arg2; # Here total is local variable.
#    print ("Inside the function local total : ", total)
#    return total
# sum( 10, 20 )
# print ("Outside the function global total : ", total )

# total=0
# def sum(a,b):
#     total=a+b
#     print(total)
#     return total
# sum(20,20)
# print(total)

##########################################
# def add_num():
#     '''input two num to get total 
#     and multiplcastion of then'''
#     total=(num1+num2)
#     print("sum of two num is:",total)
#     return total


# def multiply_num():
#     multi=(num1*num2)
#     print("multi of two num is:",multi)
#     return multi

# print(add_num.__doc__)
# num1=int(input())
# num2=int(input())
# add_num()
# multiply_num()


def fibo(n):
   res = []
   a,b = 0,1
   while b < n:
      res.append(b)
      print(b)
      prime(b)
      a, b = b, a + b
   # return res
   print(res)
def prime(b):
   if b%2 == 0:
      print("num is non prime")
   else:
      print("num is prime")
fibo(10)



