import numpy as np;

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

def chainConstructor (mainChain,flipSize):
    count = 0;
    listChain = list(mainChain);
    newChain = '';
    for i in range (len(listChain)):
        if listChain[i]== '-':
            listChain = flip (listChain,flipSize,i);
            count +=1 ;
        if listChain == "IMPOSSIBLE":
            return listChain;
        newChain = ''.join(listChain);
    return [count, newChain];


def flip (mainChain, flipSize, Index):
    alternativeChain = list(mainChain);
    if (Index+flipSize - 1) > len(alternativeChain):
        newChain = "IMPOSSIBLE";
        return newChain;
    else:
        for i in range (Index,Index+flipSize-1):
            if (alternativeChain[i]=='+'):
                alternativeChain[i]='-';
            else:
                alternativeChain [i] = '+';
        newChain = ''.join(alternativeChain);
        return newChain;


split = readLine(Lines[0]);
print(split);
mainChain = split[0];
flipsize = int(split [1]);
Constructor = chainConstructor(mainChain,flipsize);
print(Constructor);





