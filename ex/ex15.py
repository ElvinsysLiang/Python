# import argv lib from sys
from sys import argv

# there two argv, first is the program name, second is the filename
# which will be open
script, filename = argv

# use "open" funtion to open the file, and return to the parameter txt
txt = open(filename)

# print a string, tell the user what file be opened
print "Here's your file %r:" % filename
# use the read funtion of txt, and print what read
print txt.read()

# print the string to tell the user can open another file again
print "Type the filename again:"
# print the ">",and take the input to var of file_again
file_again = raw_input(">")

# open the file what be input the filename by user
txt_again = open(file_again)

# print the file contain again
print txt_again.read()
