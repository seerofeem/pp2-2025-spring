myset = {"apple", "banana", "cherry"}

thisset = {"apple", "banana", "cherry"}
print(thisset)

# Duplicate values will be ignored:
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

# True and 1 is considered the same value:
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

# False and 0 is considered the same value:
thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)

# Get the number of items in a set:
thisset = {"apple", "banana", "cherry"}

print(len(thisset))