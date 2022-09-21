# from multiprocessing.sharedctypes import Value


# dict = {1 : "hi", 2 : "hello", 3 : "welcome" , 4 : "to" , 5 : "team" , 6 :"inventam",7 : "my",
#         8 : "self" , 9 : "hiral", 10 : "done"}

# def val(func):
#     def inner(**kwargs):
#         if dict[Value] >= 5:

# def filter(**kwargs):
#     for 



####################################

# def short(): 
# for k in (class_A):
#     print(class_A[k])
# print()

# from re import /A


class_A ={"a":"riya","b":"jiyasdsc","c":"priya","d":"pridscya","e":"diya","f":"hdiya","g":"siya"}

def find(func):
    def inner(class_A):
        for key,value in class_A.copy().items():
            print(key,"->",value)
            if len(value) <= 5:
                # A = key
                # print(A)
                # print("test")
                # del class_A[A]
                del class_A[key]
        return func(class_A)
    return inner

@find      
# @short
def printer(class_A):
    print(class_A)

printer(class_A)


###############################

# class_A ={"a":"riya","b":"jiyasdsc","c":"priya","d":"pridscya","e":"diya","f":"hdiya","g":"siya"}

# # Iterating through the list of keys
# # delete = []
# for k in (class_A):
#     # print(class_A[k])
#     if len(class_A[k]) >= 5:
#         del class_A[k]
        # delete.append(class_A[k])

# print(delete)

 
# Modified Dictionary
# print(class_A[k])