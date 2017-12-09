# _*_ coding:utf-8 _*_
from sys import argv
script, input_file = argv

def print_all(f):
	print f.read()

#并没有起作用还需要解决。。
def rewind(f):
	f.seek(10, 2)

def print_a_line(line_count, f):
	f = open(input_file)
	print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)
# print "######################"
# current_file = open(input_file)
# print current_file.read()

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"
current_line = 1

print_a_line(current_line, current_file)

current_line = current_line + 1 
print_a_line(current_line, current_file)
current_line = current_line + 1 
print_a_line(current_line, current_file)