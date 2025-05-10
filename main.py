print("hello world")

# learning this lazy language for DSA

# lets go over BASICS again
print("My favorite quote is \"To be or not to be.\"") # backslash here is an escape sequence allowing user to show "" in printed text

# Math operators
2 + 3 * 6 # 20
(2 + 3) * 6 # 30
2 ** 8 # 256
23 // 7 # 23
23 % 7 # 2
(5 - 1) * ((7 + 1) / (3 - 1)) # 16.0

# Augmented Assignment operators
greeting = "Hello"
greeting += " world!"
greeting # Hello world!

number = 1
number += 1
number # 2

my_list = ['item']
my_list *= 3
my_list # ['item', 'item', 'item']

# Walrus Operator - The Walrus Operator allows assignment of variables within an expression while returning the value of the variable

print(my_var := "Hello world") # Hello world

my_var = "yes"
print(my_var) # yes

print(my_var := "hello") # hello

# Concatenation and replication

'Alice' 'Bob' # AliceBob
'Alice' * 5
# AliceAliceAliceAliceAlice

# The end keyboard

phrase = ['printed', 'with', 'a', 'dash', 'in', 'between']
for word in phrase:
    print(word, end='-')

# printed-with-a-dash-in-between-

# the sep keyboard

print('cats', 'dogs', 'mice', sep=',')
# cats,dogs,mice

