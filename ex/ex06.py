# %d equal 10, in string
x = "There are %d types of people." % 10
# put string binary to var binary
binary = "binary"
# put string don't in var do_not
do_not = "don't"

y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r," % x
print 'I also said: "%s".' % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a atring with a right side."

print w + e
