# -*- coding: utf-8 -*-
# 输出几行字符串
print "Mary had a little lamb."
# 在字符串中插入了一个字符串
print "Its fleece was white as %s." % 'snow'
print "And everywhere that Mary went."
# 这行代码很有趣，用来输出10个“.”号
print "." * 10 # what'd that do?

# 把逐个的字符一个一个放入变量中
end1 = "c"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. try removing it to see what happens
# 把end1-11的字符串起来进行输出
print end1 + end2 + end3 + end4 + end5 + end6,
# 把end7-12的字符串起来进行输出
print end7 + end8 + end9 + end10 + end11 + end12
