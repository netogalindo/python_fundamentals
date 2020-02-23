# file = open("testing_python.txt", "x") Commented because I've already created it
import os

file = open("testing_python.txt", "w") # This one is better because it doesn't result in an error if the file already
# exists

file = open("testing_python.txt", "a")
file.write("Learning Python, baby!")
file.close()

file = open("testing_python.txt", "r")
print(file.read())

file = open("testing_python.txt", "w") # This time, it's being used to overwrite content in the file
file.write("New content")
file.close()

file = open("testing_python.txt", "r")
print(file.read())

file = open("testing_python.txt", "r") # You have to do this again, everytime you want to read the file
print(file.read(7)) # This reads only the amount of characters you want to read

file = open("testing_python.txt", "w")
file.write("This is a text for me to learn how to write and read more than one line in Python.\n"
           "I will read each line soon enough.\n"
           "For now, please stand by.")

file = open("testing_python.txt", "r")
# print(file.read()) would have read everything at once
print(file.readline())
print(file.readline())
print(file.readline())

print()

# OR...

file = open("testing_python.txt", "r")
for x in file:
    print(x)
file.close() # Always close files when you are done with them

if os.path.exists("testing_python.txt"):
    os.remove("testing_python.txt") # Deletes file
    print("The file have been deleted")
else:
    print("This file does not exist")

# You can delete your entire folder with os.rmdir("name_of_the_folder"), but only if the folder is empty
