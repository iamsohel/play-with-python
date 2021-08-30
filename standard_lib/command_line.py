import sys

if len(sys.argv) == 1:
    print("USAGE: command_line.py <password>")
else:
    print("password:", sys.argv[1])
