# _*_ coding:utf-8 _*_
from sys import argv

script, filename = argv

print "We're going to erase %r." % filename

raw_input("?")

print "Opening the file..."
target = open(filename,'w')

print "Truncating the file. Goodbey!"
target.truncate()

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")

target.write(line1)
target.write("\n")
target.write(line2)

print("Close it")
target.close()

print filename
txt = open(filename)
print txt.read()



