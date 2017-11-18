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

#global variables
string = ''

print("Enter a number:")
n = int(input().strip())

for i in range(1, n+1):
    string = string + ' '


for i in range(1, n+1):
    string = string[1:]
    string = string + '#'
    print(string)
