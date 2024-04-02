#case sensitive
amrita = 1
Amrita  = 1

# variable can start with _ but not a number

price = 20.50
unit = 10

total = price*unit

#order of typecasting  - int < float
# Boolean
amrita = True
Amrita = False

number = 1
print(number)
print(Amrita)


# operation on string
sample = 'good day'
print(sample.upper())
sample = 'GOOD DAY'
print(sample.lower())


# data validation
name = 'aifoss'
number = 123456
symbol = '$'

print(name.isalpha()) # check for alphabets
print(name.isnumeric()) # check for numbers
print(name.isalnum()) # check for alphabets and numbers


print('check symbol')
print(symbol.isalnum())

sample_string = 'a quick brown fox'
# try to findout what the following syntax does
# startswith
# endswith
# find
# index

str1 = "Hello, world!"
print(str1.startswith("Hello"))  # Output: True
print(str1.startswith("world"))  # Output: False
print(str1.endswith("world!"))  # Output: True
print(str1.endswith("Hello"))    # Output: False
print(str1.find("world"))  # Output: 7
print(str1.find("universe"))  # Output: -1 returns error
print(str1.index("world"))  # Output: 7


