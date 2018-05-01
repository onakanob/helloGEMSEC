# This is a python script that opens a file whose name was passed in on the command line and echos its contents to the terminal window.

import sys # Import the commonly-used sys package - this is part of every Python installation
f = open(sys.argv[1]) # use built-in function open to access the file. sys.argv is a list of all command line arguments.
print(f.read()) # get contents of the file with read() and print them to the terminal
