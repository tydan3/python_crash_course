# DATA TYPES
# Int: Numbers w/o a decimal
-151321
654561
# Float: Numbers w/ decimal
1321.0
-9.7
# String: Anything surrounded by double or single quotes
# These strings are equivalent
'hello'
"hello"
# to include quote marks, wrap in other quote marks (i.e., single wrapped in double
#  or double wrapped in single)
'"hello"'
'"hello"'
# Bool
True
False
# OUTPUT AND PRINTING
print('OUTPUT AND PRINTING')
print(4.5)
print("hello", end='|') # end= argument sets the end of the print statement to given value
print(4.5, "hello", False, 'end') # comma-seperated values prints with a space in between
# VARIABLES
# Naming Conventions: 
#   no special characters except _
#   cannot start with number
#   use snake_case for multiword names
print("VARIABLES")
hello = 'dan'
world = "world"
world = hello
hello = 'no'
print(hello, world)
# USER INPUT
# prompt arg must be a string
print('USER INPUT')
# name = input('Name: ')
# print(name)
# age = input('Age: ')
# print('Hello', name, 'you are', age, 'years old.')
# ARITHMETIC OPERATORS
# Division always returns a float
print('ARITHMETIC OPERATORS')
x = 9
y = 3
result = x / y
print('x / y =', result)
result = x ** y # exponent
print('x ** y =', result)
result = x // y # floor division, returns int
print('x // y =', result)
result = x % y
print('x % y =', result) # mod
# num = input('Number: ')
# print(float(num) - 5) # float and int operands will result in a float result
# STRING METHODS
print('STRING METHODS')
hello = 'hElLo WorLD'
print(type(hello)) # type() returns type of given the argument, String in this case
print(hello.upper())
print(hello.lower())
print(hello.capitalize())
print(hello.lower().count('l')) # counts number of given arg in the string, capital matters
x = 'hello'
y = 3
print('hello * 3 =', x * y) # x is printed y times
y = 'world'
print(x + y) # concatenation
# CONDITIONAL OPERATORS: ==, !=, <=, >=, <, >
# chain operators (in priority order): not, and, or
print('CONDITIONAL OPERATORS')
x = "hello"
y = 'hello'
print(x == y) # double and single quotes are equivalent
print('a > Z =','a' > 'Z')
print('ASCII a =', ord('a'), 'ASCII Z =', ord('Z')) # ord returns ASCII value
print('abc' > 'aad') # compares strings left to right
print('7.0 == 7 =', 7.0 == 7)
result1 = x == y
result2 = 1 > 2
print(not(result1 or result2))
# CONDITIONS: If/Else/Elif
# print('CONDITIONS: If/Else/Elif')
# x = input('Name: ')
# if x == 'Dan':
#   print('You are great!')
# elif x == 'Tim':
#   print('Bye Tim')
# else:
#   print('This is else')
# print('Always print this')
# COLLECTIONS: List
print('COLLECTIONS: List/Tuples')
x = [4, True, 'hi'] # list can store different elements and is ordered
print(x)
print(len(x)) # length of list. len() also works on strings
x.append('hello')
print(x)
x.extend([4,5,6])
print(x)
print('x.pop(0) ->', x.pop(0))
print(x)
print('x[1] =', x[1])
x[0] = 'xyz' # lists are mutable
print(x)
y = x # y will share the same reference to list x
x[0] = 'abc'
print(x, y)
y = x[:] # y is set to a copy of list x
x[0] = 'qwerty'
print(x, y)
# Tuples: similar to list, but immutable (i.e., cannot be changed once defined)
x = (0, 0 ,2 ,2)
print(x)
# FOR LOOPS
print('FOR LOOPS')
for i in range(5, 0, -1): # start, stop, step
  print(i)
print('---')
for i in [1, 2, 3]: # iterate list
  print(i)
print('---')
x = [1, 2, 3]
for i in range(len(x)): # iterate list another way
  print(x[i])
print('---')
for i, element in enumerate(x):
  print(i, element)
# WHILE LOOPS
print('WHILE LOOPS')
i = 0
j = 3
print('i =', i, 'j = ', j)
while i < 3:
  print('i + 1')
  i += 1
  while True:
    print('j - 1')
    j -= 1
    if j <= 0:
      break
  print('i =', i, 'j = ', j)
# SLICE OPERATOR: takes a slice of a collection
# sliced = list[start:stop:step], list[:stop], list[start:], list[start:stop]
print('SLICED OPERATOR')
x = [0,1,2,3,4,5]
sliced = x[5:2:-1]
print(sliced)
s = "reverse me"
sliced = s[::-1]
print(sliced)
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
sliced = my_tuple[2:] # Slicing from index 2 to the end
print(sliced) # (3, 4, 5, 6, 7, 8, 9)
# SETS
print('SETS')
print(type({})) # dict
s = {4, 32, 2, 2} # set literal
s2 = set()
s2.add(4)
s2.add(6)
print(s2)
s.remove(32)
print(32 in s)
print(s.union(s2)) # set s + set s2
print(s.difference(s2)) # set s - set s2
print(s.intersection(s2))
# DICTIONARY: key value pair
print('DICTIONARY')
d = {'key': 4}
d['key2'] = 5
d[3] = [2,2,1,1]
print(d)
print('key' in d)
print(list(d.values()))
print(list(d.keys()))
del d[3]
print(3 in d)
for key, value in d.items():
  print(key, value)
# COMPREHENSIONS
print('COMPREHENSIONS')
x = [x for x in range(5)]
print(x)
x = {x:'value' for x in range(5)} 
print(x)
x = tuple(i for i in range(25) if i % 5 == 0)
print(x)
# FUNCTIONS
print('FUNCTIONS')
def func(x, y, z=None):
  print('run', x, y, z)
  def inner_func():
    print('hi')
  inner_func()
  return x * y, x / y # returns tuple
r1, r2 = func(5, 6)
print(r1, r2)
# ADV Example of functions: UNPACK
print('ADV Example')
def func(x):
  def func2():
    print(x)
  return func2
x = func(3)
x()
# *args, **kwargs
print('*args, **kwargs')
