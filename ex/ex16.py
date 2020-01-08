# -*- coding:utf-8  -*-

# 从sys库中提取argv模板
from sys import argv
# 设置两个参数，一个是程序名本身，一个是需要打开文件的文件名
script, filename = argv
# 输出提示信息，将会打开哪个文件，不想打开就ctrlC，继续打开就回车
print "We're going to erase %r." % filename
print "If you don't want that. hit CTRL-C."
print "If you do want that, hit RETURN."
# 输出一个“？”提示用户输入ctrl+c或者回车
raw_input("?")
# 因为不是ctrl+c，所以继续打开，显示一段提示信息
# 其实这里可能加入错误检查会比较好
print "Opening the file..."
# 这里其实可以理解为类似Linux的文件描述符，当然，这里其实是创建一个对象了
target = open(filename, 'w')
# 显示一段提示，并清空了这个文件
print "Truncating the file. Goodbye!"
# target.truncate()
# 显示一段提示，读入三个字符串并存储到三个变量之中
print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")
# 显示一段提示，并把三个变量，以及变量间的换行符逐一输入到文件中
print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
print "line1: %s\nline2: %s\nline3: %s\n" % (line1, line2, line3)

# 显示一段结束信息，并删除了这个文件对象，和关闭文件描述符释放资源差不多
print "And finally. we close it."
target.close()

