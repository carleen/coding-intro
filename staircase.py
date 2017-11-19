'''For any given number n, create a staircase composed of that number of 
rows/ colums. Example below:
n = 5
    #
   ##
  ###
 ####
#####
'''

import sys

#global variable
string = ''

#Asks user for input, and converts to integer
print("Enter a number:")
n = int(input().strip())

#Creates an initial string of spaces of n length
for ii in range(1, n+1):
    string = string + ' '

#Removes the first space from the string, adds a # to the end
for ii in range(1, n+1):
    string = string[1:]
    string = string + '#'
    print(string)
