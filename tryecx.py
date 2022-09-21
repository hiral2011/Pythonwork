# def someone(x,y):
#     try:
#         result = x//y
#         print("someone is ryt ans is :",result)
#     except ZeroDivisionError:
#         print("i m out,need ammo")

# someone(30,10)
# someone(30,0)

##########################

# def AbyB(a , b):
#     try:
#         c = ((a+b) // (a-b))
#     except ZeroDivisionError:
#         print ("a/b result in 0")
#     else:
#         print (c)
  
# # Driver program to test above function
# # AbyB(5, 10)
# AbyB(7, 2)

####################

# try:
#     k = 15//0 # raises divide by zero exception.
#     print(k)
    
# except ZeroDivisionError:   
#     print("Can't divide by zero")
        
# finally:
#     print('This is always executed') 


############################

try:
    example()
except RuntimeError as e:
    print("It didn't work:", e)
    if e.__cause__:
        print('Cause:', e.__cause__)