#!/usr/bin/python

"""
A module is a file containing Python definitions and statements.
The file name is the module name with the suffix .py appended.

A module can contain executable statements as well as fuction definitions. These statements are
intended to initialize the module. They are executed only the first time the module name is
encountered in an import statement. They also run if the file is executed as a script.

It is also possible to import all names from a module into the current namespace by using the following
import statement

from modulename import *

However this statement also exhausts on resources and should be used sparingly

"""

# Below is a sample of the module rider in play:

import rider


def calculate(arg1, arg2):
	ans = rider.add(arg1,arg2)
	# the method add() is called to execute an addition of inputed values


calculate(10, 15)

rider.hi()
