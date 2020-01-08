import time

numbers = []

def creat_arr(iNum):
    i = 0
    iNum = int(iNum)
    print "iNum is %d" % iNum
    while i < iNum:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
        time.sleep(1)    
print "input the num to create a array:"
iNum = raw_input(">")
creat_arr(iNum)
print "The numbers: "

for num in numbers:
    print num






