# List comprehension 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

# Short hand 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

# Only accept items that are not "apple":
newlist = [x for x in fruits if x != "apple"]
print(newlist)

# With no if statement:
newlist = [x for x in fruits]
print(newlist)
# You can use the range() function to create an iterable:
newlist = [x for x in range(10)]
print(newlist)
# Accept only numbers lower than 5:
newlist = [x for x in range(10) if x < 5]
print(newlist)
# Set the values in the new list to upper case:
newlist = [x.upper() for x in fruits]
print(newlist)
# Set all values in the new list to 'hello':
newlist = ['hello' for x in fruits]
print(newlist)
# Return "orange" instead of "banana":
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

#####################################################

# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# Sort the list numerically:
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# Sort the list descending:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

# Sort the list based on how close the number is to 50:
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

# Perform a case-insensitive sort of the list:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

# Reverse the order of the list items:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)