# -*- coding: utf-8 -*-

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

# 使用函数，但在参数中的算是整数？还是字符串？
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)


print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
# 把上面定义的两个参数装填到函数中，使用函数进行print
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# 用这个函数来进行数学计算，在参数的位置就计算完成，然后
# 直接把参数填入函数体进行print
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)


# 打印一个信息，说明这个函数被用作数学计算
print "And we can combine the two, variables and math:"
# 把之前定义的两个整数加上另一个整数作为参数传入函数当中
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

