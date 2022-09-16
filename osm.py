# import os 
    
# # Function to Get the current  
# # working directory 
# def current_path(): 
#     print("Current working directory before") 
#     print(os.getcwd()) 
#     print() 
    
    
# # Driver's code 
# # Printing CWD before 
# current_path() 
    
# # Changing the CWD 
# os.chdir('../') 
    
# # Printing CWD after 
# current_path() 

########################   make dir

import os
print(os.mkdir("inventam"))
print(os.mkdir("inventam2"))
print(os.rmdir("/home/hiral/inventam2"))

print(os.chdir("/home/hiral"))
print(os.chdir("/home//"))

print(os.listdir("/home/hiral/Desktop"))
print(os.listdir())
print(os.listdir())

