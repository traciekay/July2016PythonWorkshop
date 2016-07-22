"""
Functions

NOTE: functions can take parameters in order to achieve specific processing needs
"""



#function with one argument
def print_one(odm):
    print "odm: %r" %odm

def print_arg(odm):
	print odm

#function with two arguments
def print_two(odm, tna):
    print "odm: %r, tna: %r" %(odm, tna)


#function with no arguments
def print_none():
    print "Nothing to see."


print_two("Moringa", "School")
print_one("MS")
print_none()
print_arg("Jojo")
