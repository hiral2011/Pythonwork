f = open("msg.txt",'r')

try:

    content = f.read()
    print(content)

    more_content = f.read()
    print(more_content)

finally:
    f.close()

###################2nd method also if you want some particular line or word or part o file

with open("msg.txt",'r') as f:  


    file1 = f.read(6)
    print(file1)

    more_content = f.read(9)
    print(more_content)

########################add (update) file

with open("python.txt","a")as f:
    f.write("\npython is my fav programing language")

###########################

with open("python.txt","r") as f:

    lines = f.readlines()
    print(lines)

#######################

myfile1 = open("msg.txt", "w")

print("myfile1.isatty():", myfile1.isatty())
myfile1.close()

##############################

with open("msg.txt",'w') as f:  
    f.write("hello line 2\n")
    f.write(" line 3\n")

##### only write when u write the old msg deleted

with open("msg.txt",'w') as f:  
    f.write("hello line 4\n")
    f.write(" line 35\n")


#######if you want you old and add new line you use append

with open("msg.txt",'a') as f:  
    f.write("hello line 7\n")
    f.write(" line 52\n")

######################read and write

with open("msg.txt",'r+') as f:  
    # f.write("this line is add at a operatin time or read and write test\n")
    file1 = f.read()
    print(file1)

    more_content = f.read()
    print(more_content)

###############write and read 

with open("msg.txt",'w+') as f:  
    f.write("i m also a new line added at the time of write and read test\n")

    file1 = f.read()
    print(file1)

    more_content = f.read()
    print(more_content)

#####################
with open("msg.txt",'w+') as f:  
    f.write("i m also a new line22 added at the time of write and ead test\n")
    f.write("i m also a new line23 added at the time of write and ead test\n")
    f.write("i m also a new line24 added at the time of write and ead test\n")
    f.write("i m also a new line25 added at the time of write and ead test\n")

    file1 = f.read()
    print(file1)

    more_content = f.read()
    print(more_content)

##################################

with open("Sample.json", "w") as p:
     json.dump(var, p)







