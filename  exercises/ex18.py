# _*_ coding:utf-8 _*_
# this one is like your scripts with argv
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

#一定要注意缩进
print_two("Zed", "args")

def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)
print_two_again("zed", "print")

def print_one(arg1):
	print "arg1: %r" % arg1
print_one("print_one")

def print_none():
	print "I got nothin"
print print_none()

