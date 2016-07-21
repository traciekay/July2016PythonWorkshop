#functions




#function with one argument
def print_one(arg1):
    print "arg1: %r" %arg1

def print_arg(arg1):
	print arg1

#function with two arguments
def print_two(arg1, arg2):
    print "arg1: %r, arg2: %r" %(arg1, arg2)


#function with no arguments
def print_none():
    print "Nothing to see."


print_two("Moringa", "School")
print_one("MS")
print_none()
print_arg("Jojo")
