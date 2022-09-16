# from logging import exception
import sys
# x = 1
# y = 0
# assert y != 0, "Invalid Operation" # denominator can't be 0
# print(x / y)

##############

# x = 1       #right
# y = 0
# assert y == 0, "Invalid Operation" # denominator can't be 0
# print(x / y)

################

# try:                
#     x = 1               #in this this will prtint msg what we give  in it to below
#     y = 0                   #also  want except part              
#     assert y != 0, "Invalid Operation"
#     print(x / y)/
 
# the errror_message provided by the user gets printed
# except AssertionError as msg:
#     print(msg)

########################

# print(sys.platform)
# if not sys.platform.startswith("windows"):
#     raise exception("opps....")

# if not sys.platform.startswith("linux"):
#     raise exception("opps....")
# print("welcome")

# class wrongerror(Exception):
#     pass

# if not sys.platform.startswith("windows"):
#     raise wrongerror("opps....wrong os")
# print("welcome")

#########################

# try:
#     with open('file.log') as file:
#         read_data = file.read()
# except:
#     print('Could not open file.log')

######################

# try:
#     with open('file.log') as file:
#         read_data = file.read()
# except FileNotFoundError as fnf_error:
#     print(fnf_error)

##############################

# try:
#     linux_interaction()
#     with open('file.log') as file:
#         read_data = file.read()
# except FileNotFoundError as fnf_error:
#     print(fnf_error)
# except AssertionError as error:
#     # print(error)
#     print('Linux linux_interaction() function was not executed')

#######################3333

# try:
#     linux_interaction()
# except AssertionError as error:
#     print(error)
# else:
#     print('Executing the else clause.')


###############################

# import math
# def ShridharAcharya(a, b, c):
#     try:
#         assert a != 0, "Not a quadratic equation as coefficient of x ^ 2 can't be 0"
#         D = (b * b - 4 * a*c)
#         assert D>= 0, "Roots are imaginary"
#         r1 = (-b + math.sqrt(D))/(2 * a)
#         r2 = (-b - math.sqrt(D))/(2 * a)
#         print("Roots of the quadratic equation are :", r1, "", r2)
#     except AssertionError as msg:
#         print(msg)
# ShridharAcharya(-1, 5, -6)
# ShridharAcharya(1, 1, 6)
# ShridharAcharya(2, 12, 18)

########################################



# try:
#     n = int(input())
#     print(n * 10)
    
# except EOFError as e:
#     print(e)


################

def print_even(test_list):
    for i in test_list:
        # print(i)
        if i % 2 != 0:
            yield i
            # print(i)
 
# initializing list
test_list = [1, 4, 5, 6, 7]
 
# printing initial list
print("The original list is : " + str(test_list))
 
# printing even numbers
print("The even numbers in list are : ", end=" ")
for j in print_even(test_list):
    print(j, end=" ")

##############################

# def nextSquare():
#     i = 1
 
#     # An Infinite loop to generate squares
#     while False:
#         yield i*i
#         # Next execution resumes from this point
#         i += 1
        
# # Driver Code
# for num in nextSquare():
#     if num > 100:
#         break
#     print(num)

##############################

# try:
#     div_by_zero = 10/0
# except Exception as e:
#     print(f"Exception name:{e}")
# else:
#      print("I would have run if there wasn't any exception")
# finally:
#     print("I will always run!")


################################3

# def generator():
#  print("Hello this is the 1st element")
#  yield 5
#  print("Hello this is the 2nd element")
#  yield 15
#  print("Hello this is the 3rd element")
#  yield 25
#  print("Hello this is the 4th element")
#  yield 35

# g = generator()
# print(next(g))
# print(next(g))
