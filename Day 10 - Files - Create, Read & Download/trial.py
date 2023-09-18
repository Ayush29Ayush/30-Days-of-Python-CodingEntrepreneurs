fname = "Day 10 - Files - Create, Read & Download\hello-world.txt"


#! Noob way 
# file_object = open(fname, "w")
# file_object.write("Hello world")
# file_object.close()

#! Optimised way -> It opens and closes the file for me automatically
# with open(fname, "w") as file_object:
#     file_object.write("Hello world again")
with open(fname, "r") as f:
    print(f.read())
    
