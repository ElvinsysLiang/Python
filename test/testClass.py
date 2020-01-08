class person(object):
    def __init__(self, age):
        self.age = age
    def get_age(self):
        print "age is %d" % self.age

print "create a person instance tom and"
tom = person(31)
tom.get_age()
