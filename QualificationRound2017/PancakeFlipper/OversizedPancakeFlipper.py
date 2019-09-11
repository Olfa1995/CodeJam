import numpy as np
#Library that adds support for multi-dimensional arrays and matrices

# Read Input File
# Open function takes the path as first argument. We do not need to use the full path when the file is in the working directory
# The second argument of open could be 'r' for reading , 'w' for writing and other options. Here we need to read the file.
# <file>.read returns the entire contents of the file as a single string.

Input = open("A-small-practice.in",'r').read();

#Converts the long string to an array of rows split "/n" (return to the line). The rows are the lines of the input

Lines = [s.strip() for s in Input.splitlines()];
Lines = np.delete(Lines, (0), axis=0); #Deletes the first row that has the number of cases

def readLine(line):
   split  = line.split();
   return split

def Flip (split):
    count = 0;
    for val in split[0]:
        if val == '-':
            val = '+';
            count +=1;
    return [split[0], count];

split = readLine(Lines[0]);
Flip = Flip (split);
print (Flip);


