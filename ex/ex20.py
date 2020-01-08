# -*- coding:utf-8 -*-
from sys import argv

script, input_file = argv
# 传入文件对象，打印整个文件的内容
def print_all(f):
    print f.read(),
# 设置输出的位置为0
def rewind(f):
    f.seek(0)
# 传入行号和文件对象，并打印行号和单行
def print_a_line(line_count, f):
    print line_count, f.readline(),

current_file = open(input_file)
# 打印整个文件的内容
print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."
# 设置打印的位置从0开始
rewind(current_file)

print "Let's print three lines:"
# 行号设置从1开始，打印第一行行号以及内容
current_line = 1
print_a_line(current_line, current_file)
# 行号+1，打印第二行行号以及内容
current_line = current_line + 1
print_a_line(current_line, current_file)
# 行号+1，打印第三行行号以及内容
current_line = current_line + 1
print_a_line(current_line, current_file)



