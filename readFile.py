# Two ways to call a custom function from an external python package. say() takes a file name as an argument and prints its contents to the terminal window

from batchExample.scripts import say #import just one function
import batchExample.scripts as myScripts #import a whole package and give it a local name

f = open('./batchExample/1.txt') # open() is a built-in function. Use it to start reading from a file
say(f.read()) #here's the function i imported. Use the open file's member function read() to pass the file's contents to say()
f.close # close the file

f = open('./batchExample/2.txt') # Again with a different text file...
myScripts.say(f.read()) # This time, give the file's contents to a member function of the package batchExample.scripts, which was renamed myScripts
f.close # close the file
