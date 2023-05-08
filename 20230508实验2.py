import sys
import os


file=open("a.txt","w")
file.write("Python,C,Java,SQL,Basic\n")
file.flush()
file.close()

file=open("a.txt","r")
lines = file.readlines()
for line in lines:
    line = line.strip('\t')
    print(line)

file.close()