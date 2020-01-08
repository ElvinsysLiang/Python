class Parent(object):

    def implicit(self):
        print "PARENT implicit()"

class Chile(Parent):

    pass

dad = Parent()
son = Chile()

dad.implicit()
son.implicit()

