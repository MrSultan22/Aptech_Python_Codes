#====================<<Strings and methods>>=======================
print('====================<<simple string>>====================')
poem = 'Ode to a Nightingale'

lyric = "Roll on, Columbia, roll on"

exclamation = "That makes me !#? "

#The empty string has zero characters ('' or "")
print("poem:",poem,'\nlyric: ',lyric, '\nexclamation: ', exclamation)

print('==========<<Putting a format character in a string>>=========')

# A newline is represented by '\n'
print('Good night, good night\nParting is such sweet sorrow')

# A tab is represented by '\t'
print('col0\tcol1\tcol2')
# with backslash you can do more.

print('==========<<Index of string characters>>=========')

name = "my name is sultan!" # string also counting the space in string value.
# In this string value total index is 12.
# it finde index of sultan in string valu.
print("sultan is on ",name.index('sultan') ,'index')

print('--------------------------------------------')
#The first character of a string has index 0. 
greeting = 'hello, world'
# it will print first letter that is on zero index.
print( greeting[0])

#--------------------------------------------
#You can also count back from the end of a string, beginning with -1. 
greeting = 'hello, world'
# it will print last first letter that is on 11 index .
print( greeting[-1])

print('==========<<Slicing a string>>=========')
# You can use indexes to slice (extract a piece of) a string.
# aStr[i:j] is the substring that begins with index i and ends
# with (but does not include) index j.
# syntax for slicing = [start:end:steps that will be skip].
name1 = 'sultan is here.'
print(name1[1:3])  # here given only starting and ending points.
print(name1[1:7:2])# here given only starting, ending and steps  points.
print(name1[-3:-1])


