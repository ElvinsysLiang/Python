# -*- coding:utf-8 -*-

# there are something wrong in the program
# I want to var1 + var2, but the result is 
# the two string cat in one string! Why???????
# I know!it must be put the var into int()
# then the var become a int type

print "Now, I want to test the define funtion!\n"

def _a5(var1, var2):
    var1 = int(var1)
    var2 = int(var2)
    return int(var1 + var2)

var1 = raw_input("var1: ")
var2 = raw_input("var2: ")

# print "%d + %d = %d\nfinish!\n", % (var1, var2, _a5(var1, var2))
print _a5(var1, var2)
